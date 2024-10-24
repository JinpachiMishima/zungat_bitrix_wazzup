import os
import logging

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
# from dotenv import load_dotenv

from task import send_messages
from conf.conf_log import setup_logging
# Creates a default Background Scheduler

# load_dotenv()

setup_logging()
logger = logging.getLogger(__name__)
days = ["mon","tue","wed","thu","fri","sat","sun"]
send_message_day = days[int(os.getenv("day"))]
send_message_hour = int(os.getenv("hour"))
send_message_minute = int(os.getenv("minute"))

scheduler = BlockingScheduler()

scheduler.add_job(send_messages, CronTrigger(
    day_of_week=send_message_day, 
    hour=send_message_hour, 
    minute=send_message_minute
    ))

if __name__ == "__main__":
    logger.info("Start program {day}-{hour}:{minute}".format(
        day=send_message_day,
        hour=send_message_hour,
        minute=send_message_minute
    ))
    scheduler.start()