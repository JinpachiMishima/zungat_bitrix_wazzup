import logging
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
 
from task import send_messages
from conf.conf_data import (
    send_message_day,
    send_message_hour,
    send_message_minute
    
)
from conf.conf_log import setup_logging
# Creates a default Background Scheduler


setup_logging()
logger = logging.getLogger(__name__)


scheduler = BlockingScheduler()

scheduler.add_job(send_messages, CronTrigger(
    day_of_week=send_message_day, 
    hour=send_message_hour, 
    minute=send_message_minute
    ))

if __name__ == "__main__":
    logger.info("Start program")
    scheduler.start()