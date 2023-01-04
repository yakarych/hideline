import asyncio
from typing import Optional

from aiogram import Bot
from glQiwiApi import YooMoneyAPI
from glQiwiApi.yoo_money.types import OperationHistory, Operation

from app.models.database import User
from app.services.api.connector import get_connection
from app.services.database.dao.user import UserDAO
from app.services.payments.types import Cost, get_payment_type
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
            for user in await dao.get_all():
                print("Текущий каунт: ", user.payments_count)
                payments_history = await client.operation_history(records=100, label=str(user.id))
                new_payment = self._get_new_payment_if_exists(payments_history=payments_history, user=user)
                if new_payment:
                    await dao.increment_payments_count(user_id=user.id)
                    payment_amount = get_payment_type(new_payment.amount)
                    connection = get_connection()
                    count = self._get_bought_keys_count(payment_amount)

                    for _ in range(count):
                        new_key = connection.create_key(key_name=str(user.id))
                        connection.add_data_limit(new_key.key_id, 1024 * 1024 * 1024 * 30)  # 30GB
                        await self.bot.send_message(user.id, f"Вы купили ключ, поздравляю! "
                                                             f"Скопируйте и вставьте его в Outline:\n "
                                                             f"<code>{new_key.access_url}</code>")
                        await asyncio.sleep(0.1)

    def _get_bought_keys_count(self, payment_amount: Cost) -> int:
        if payment_amount == Cost.ONE_KEY_COST:
            return 1
        elif payment_amount == Cost.TWO_KEY_COST:
            return 2
        elif payment_amount == Cost.THREE_KEY_COST:
            return 3
        return 0

    def _get_new_payment_if_exists(self, payments_history: OperationHistory, user: User) -> Optional[Operation]:
        personal_operations = []
        for operation in payments_history.operations:
            if operation.status == "success" and operation.label == str(user.id) and operation.direction == 'in':
                personal_operations.append(operation)
                print('Операция ', operation)

        if personal_operations:
            # Skipped user without new (actual) payments
            if len(personal_operations) <= user.payments_count:
                return None
            for operation in personal_operations:
                if get_payment_type(amount=operation.amount):
                    return operation
        return None


def get_payment_url(user_id: int, cost: Cost) -> str:
    return YooMoneyAPI.create_pay_form(
        receiver=load_config().yoomoney_api.card_id,
        quick_pay_form="shop",
        targets="Hideline",
        payment_type="SB",
        amount=cost.value,
        label=str(user_id)
    )
