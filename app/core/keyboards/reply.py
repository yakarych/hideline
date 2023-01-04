from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.core.navigations import reply


class ResizedReplyKeyboard(ReplyKeyboardMarkup):
    """
    I prefer override default ReplyKeyboardMarkup to avoid passing the resizer parameter
    every time.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize_keyboard = True


default_menu = ResizedReplyKeyboard(
    keyboard=[
        [
            KeyboardButton(reply.create_access_key),
            KeyboardButton(reply.access_keys),
        ],
        [
            KeyboardButton(reply.support),
        ]
    ]
)
