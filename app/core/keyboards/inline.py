from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.services.payments.types import Cost

keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"1 ключ — {Cost.ONE_KEY_COST.value} руб.", callback_data="buy_keys_1"),
        ],
        [
            InlineKeyboardButton(text=f"2 ключа — {Cost.TWO_KEY_COST.value} руб.", callback_data="buy_keys_2"),
        ],
        [
            InlineKeyboardButton(text=f"3 ключа — {Cost.THREE_KEY_COST.value} руб.", callback_data="buy_keys_3"),
        ]
    ]
)