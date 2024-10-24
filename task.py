import os
import time
import logging


from api.bx.bx_api import BX
from api.wz.wz_api import WZ
from api.wz.message import Message
from conf.conf_log import setup_logging


setup_logging()

logger = logging.getLogger(__name__)

bitrix_token = os.getenv("BITRIX_TOKEN")
wazzup_token = os.getenv("WAZZUP_TOKEN")
channel_id = os.getenv("wazzup_channel_id")
bitrix_category_id = os.getenv("category_id")
bitrix_stage_id = os.getenv("stage_id")
message_text = os.getenv("text")

def correct_phone_number(phones):
    if len(phones) > 0:
        phone_number = phones[0].value
        phone_number = "".join([i for i in phone_number if i in [
            "0","1","2","3","4","5","6","7","8","9","0"]])
        phone_number = "7" + phone_number[-10:]
    else:
        phone_number = None
    return phone_number

def correct_balance(balance):
    if balance is None:
        balance = 0
    return balance

def send_messages():
    logger.info("Start schedule")
    start = time.time()
    bx = BX(bitrix_token)
    wz = WZ(wazzup_token)

    deals = bx.get_deals(
        category_id=bitrix_category_id,
        stage_id=bitrix_stage_id
        )

    contacts_id = []
    for deal in deals:
        if deal.client_id != None:
            contacts_id.append(deal.client_id)
    contacts_id = list(set(contacts_id))
    contacts = bx.get_contacts(contacts_id=contacts_id)
    logger.info(f"All correct contacts: {len(contacts)}")

    for contact in contacts:
        message = Message(
            channel_id=channel_id,
            chat_type="whatsapp",
            chat_id=correct_phone_number(contact.phones),
            text=message_text.format(
                user_name=contact.first_name,
                balance=correct_balance(contact.balance)
                )
        )
        # logger.info(f"send message to {correct_phone_number(contact.phones)}")
        wz.send_message(message=message)    # отправка сообщения в вазап
    logger.info(f"{time.time() - start}")
