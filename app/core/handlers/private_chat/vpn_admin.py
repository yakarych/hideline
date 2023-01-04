from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType

from app.core.middlewares.throttling import throttle


@throttle(limit=2)
async def cmd_get_data(m: types.Message, state: FSMContext):
    """Sends f"""


def register_handlers(dp: Dispatcher) -> None:
    """Register base handlers: /start and handling events from default menu"""

    dp.register_message_handler(cmd_get_data, commands="data",
                                chat_type=ChatType.PRIVATE, vpn_admin=True, state="*")
