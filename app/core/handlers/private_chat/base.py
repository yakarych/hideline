import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ChatType, ChatActions

from app.core.keyboards import reply, inline
from app.core.messages.private_chat import base as msgs
from app.core.middlewares.throttling import throttle
from app.core.navigations.command import Commands
from app.models.dto import get_user_from_message
from app.core.navigations import reply as reply_texts
from app.services.api.connector import get_connection
from app.services.database.dao.user import UserDAO


@throttle(limit=3)
async def cmd_start(m: types.Message, state: FSMContext):
    """/start command handling. Adds new user to database, finish states"""
    await state.finish()

    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.welcome(user_firstname=user.firstname))
    await m.answer_chat_action(ChatActions.TYPING)
    await asyncio.sleep(1)

    await m.answer(msgs.instruction, reply_markup=reply.default_menu)


@throttle(limit=3)
async def cmd_instruction(m: types.Message, state: FSMContext):
    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.instruction, reply_markup=reply.default_menu)


@throttle(limit=2)
async def create_keys(m: types.Message, state: FSMContext):
    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)
    await m.answer(msgs.keys_description)
    await m.answer_chat_action(ChatActions.TYPING)
    await asyncio.sleep(1)
    await m.answer(msgs.keys_description_2, reply_markup=inline.keys(user_id=user.id))


@throttle(limit=4)
async def my_keys(m: types.Message, state: FSMContext):
    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)

    api_connection = get_connection()
    user_keys = [key for key in api_connection.get_keys() if key.name == str(user.id)]
    for i, key in enumerate(user_keys):
        await m.answer(f"<b>{i+1}</b>. Ключ: <code>{key.access_url}</code>\n")
    if not user_keys:
        await m.answer("У тебя нет ключей. Купи и будут!)")


def register_handlers(dp: Dispatcher) -> None:
    """Register base handlers: /start and handling events from default menu"""

    dp.register_message_handler(cmd_start, commands=str(Commands.start),
                                chat_type=ChatType.PRIVATE, state="*")
    dp.register_message_handler(cmd_instruction, commands=str(Commands.instruction),
                                chat_type=ChatType.PRIVATE, state="*")
    dp.register_message_handler(create_keys, commands=str(Commands.create_key),
                                chat_type=ChatType.PRIVATE, state="*")
    dp.register_message_handler(create_keys, Text(reply_texts.create_access_key))
    dp.register_message_handler(my_keys, commands=str(Commands.access_keys),
                                chat_type=ChatType.PRIVATE, state="*")
    dp.register_message_handler(my_keys, Text(reply_texts.access_keys))
