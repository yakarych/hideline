from typing import Iterable, Optional, List

from aiogram import Bot
from glQiwiApi import YooMoneyAPI
from glQiwiApi.yoo_money.types import OperationHistory, Payment, Operation

from app.models.database import User
from app.services.database.dao.user import UserDAO
from app.services.payments.types import Cost, MAX_RUB_COMMISSION_VALUE, get_payment_type
from app.settings.config import load_config


COMMISSION_AMOUNT = 20


class PaymentsChecker:
    bot: Bot
    yoomoney_token: str

    def __init__(self, bot: Bot, yoomoney_token: str):
        self.bot = bot
        self.yoomoney_token = yoomoney_token

    async def check(self) -> None:
        dao = UserDAO(session=self.bot.get("db"))
        async with YooMoneyAPI(api_access_token=self.yoomoney_token) as client:
            payments_history = await client.operation_history(records=30)
            for user in await dao.get_all():
                new_payment = self._get_new_payment(user_id=user.id, payments_history=payments_history, user=user)
                if new_payment:
                    await dao.increment_payments_count(user_id=user.id)
                    print(new_payment)
                    print(user)

    def _get_new_payment(self, user_id: int, payments_history: OperationHistory, user: User) -> Optional[Operation]:
        payments_history.operations = self._get_personal_operations(
            operations=payments_history.operations,
            user_id=user_id
        )
        if payments_history.operations:
            # Skipped user without new (actual) payments
            if len(payments_history.operations) <= user.payments_count:
                return None

            for operation in payments_history.operations:
                if operation.status == "success" and get_payment_type(amount=operation.amount):
                    return operation
        return None

    def _get_personal_operations(self, operations: Iterable, user_id: int) -> Optional[List]:
        return [operation for operation in operations if str(user_id) in operation.label and operation.status == "success"]


def get_payment_url(user_id: int, cost: Cost) -> str:
    return YooMoneyAPI.create_pay_form(
        receiver=load_config().yoomoney_api.card_id,
        quick_pay_form="shop",
        targets="Hideline",
        payment_type="SB",
        amount=cost.value,
        label=f"{user_id}{cost.value}"
    )
