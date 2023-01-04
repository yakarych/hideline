from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.services.payments.billing import get_payment_url
from app.services.payments.types import Cost


def keys(user_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"1 ключ — {Cost.ONE_KEY_COST.value} руб.", url=get_payment_url(user_id, Cost.ONE_KEY_COST)),
            ],
            [
                InlineKeyboardButton(text=f"2 ключа — {Cost.TWO_KEY_COST.value} руб.", url=get_payment_url(user_id, Cost.TWO_KEY_COST)),
            ],
            [
                InlineKeyboardButton(text=f"3 ключа — {Cost.THREE_KEY_COST.value} руб.", url=get_payment_url(user_id, Cost.THREE_KEY_COST)),
            ]
        ]
    )
