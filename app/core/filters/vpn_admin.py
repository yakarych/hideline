from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

ADMIN_IDS = (5105430766, )


class VPNAdminFilter(BoundFilter):
    """
    Check if the user is a bot admin
    """

    key = "vpn_admin"

    def __init__(self, project_admin: bool):
        self.project_admin = project_admin

    async def check(self, obj: Union[types.Message, types.CallbackQuery]):
        user = obj.from_user
        if user.id in ADMIN_IDS:
            return self.project_admin is True
        return self.project_admin is False
