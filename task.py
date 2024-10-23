import os
import time

from dotenv import load_dotenv

from api.bx.bx_api import BX
from api.wz.wz_api import WZ
from api.wz.message import Message



load_dotenv()
bitrix_token = os.getenv("BITRIX_TOKEN")
wazzup_token = os.getenv("WAZZUP_TOKEN")

def task1():

    start = time.time()
    bx = BX(bitrix_token)
    wz = WZ(wazzup_token)

    deals = bx.get_deals(category_id=9,stage_id="C9:PREPAYMENT_INVOICE")

    contacts_id = []
    for deal in deals:
        if deal.client_id != None:
            contacts_id.append(deal.client_id)
    contacts_id = list(set(contacts_id))
    contacts = bx.get_contacts(contacts_id=contacts_id)
    print(f"всего подходящих контактов: {len(contacts)}")

    for contact in contacts:
        message = Message(
            channel_id="5413949d-f706-4774-bb1c-f6e2055a90ec",
            chat_type="whatsapp",
            chat_id=contact.phone,
            text=f"Ассаламу аллейкум {contact.first_name}, ваш баланс {contact.balance} рублей"
        )
        print(message)
        # wz.send_message(message=message)
    
    
    print(time.time() - start)

task1()