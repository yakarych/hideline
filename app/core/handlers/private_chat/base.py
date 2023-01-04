import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType, ChatActions

from app.core.keyboards import reply
from app.core.messages.private_chat import base as msgs
from app.core.middlewares.throttling import throttle
from app.core.navigations.command import Commands
from app.models.dto import get_user_from_message
from app.services.api import connector
from app.services.database.dao.user import UserDAO


@throttle(limit=2)
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
    print(connector.get_connection().get_keys())


def register_handlers(dp: Dispatcher) -> None:
    """Register base handlers: /start and handling events from default menu"""

    dp.register_message_handler(cmd_start, commands=str(Commands.start),
                                chat_type=ChatType.PRIVATE, state="*")
    dp.register_message_handler(cmd_instruction, commands=str(Commands.instruction),
                                chat_type=ChatType.PRIVATE, state="*")
