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
            payments_history = await client.operation_history(records=100)
            for user in await dao.get_all():
                new_payment = self._get_new_payment_if_exists(payments_history=payments_history, user=user)
                print('Нью')
                print(new_payment)
                if new_payment:
                    print('инкремент')
                    await dao.increment_payments_count(user_id=user.id)
                    print(await dao.get_by_id(user.id))
                    print('Новая оплата')
                    print(new_payment)
                    print(user)

    def _get_new_payment_if_exists(self, payments_history: OperationHistory, user: User) -> Optional[Operation]:
        personal_operations = []
        for operation in payments_history.operations:
            if str(user.id) in str(operation.label) and operation.status == "success":
                personal_operations.append(operation)

        if personal_operations:
            # Skipped user without new (actual) payments
            print(personal_operations)
            if len(personal_operations) <= user.payments_count:
                return None
            print(personal_operations, user.payments_count)
            for operation in personal_operations:
                if operation.status == "success" and get_payment_type(amount=operation.amount):
                    return operation
        return None


def get_payment_url(user_id: int, cost: Cost) -> str:
    return YooMoneyAPI.create_pay_form(
        receiver=load_config().yoomoney_api.card_id,
        quick_pay_form="shop",
        targets="Hideline",
        payment_type="SB",
        amount=cost.value,
        label=f"{user_id}_{cost.value}"
    )
