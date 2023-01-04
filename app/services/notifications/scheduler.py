from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.services.payments.billing import PaymentsChecker
from app.settings.config import Config


def setup_cron_jobs(scheduler: AsyncIOScheduler, bot: Bot, config: Config) -> None:
    scheduler.add_job(
        func=PaymentsChecker(
            bot=bot,
            yoomoney_token=config.yoomoney_api.token
        ).check,
        trigger=IntervalTrigger(seconds=15),
    )
