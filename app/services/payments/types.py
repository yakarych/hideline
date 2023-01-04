from enum import Enum
from typing import Optional


class Cost(int, Enum):
    ONE_KEY_COST = 150
    TWO_KEY_COST = 250
    THREE_KEY_COST = 300


MAX_RUB_COMMISSION_VALUE = 30


def get_payment_type(amount: float) -> Optional[Cost]:
    if Cost.ONE_KEY_COST.value - MAX_RUB_COMMISSION_VALUE <= amount <= Cost.ONE_KEY_COST.value + MAX_RUB_COMMISSION_VALUE:
        return Cost.ONE_KEY_COST
    if Cost.TWO_KEY_COST.value - MAX_RUB_COMMISSION_VALUE <= amount <= Cost.TWO_KEY_COST.value + MAX_RUB_COMMISSION_VALUE:
        return Cost.TWO_KEY_COST
    if Cost.THREE_KEY_COST.value - MAX_RUB_COMMISSION_VALUE <= amount <= Cost.THREE_KEY_COST.value + MAX_RUB_COMMISSION_VALUE:
        return Cost.THREE_KEY_COST
    return None
