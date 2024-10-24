import logging

from bitrix24 import Bitrix24

from api.bx.bx_deal import Deal
from api.bx.bx_contact import Contact
from conf.conf_log import setup_logging


setup_logging()
logger = logging.getLogger(__name__)

class BX:
    def __init__(self,token):
        self.token = token
        self.bx24 = Bitrix24(token)
    
    def get_deals(self,category_id,stage_id):
        logger.info("request deals from {stage_id}".format(stage_id=stage_id))
        answ = self.bx24.callMethod(
            method="crm.deal.list",
            params={
                "filter":{
                    "CATEGORY_ID":category_id,
                    "STAGE_ID":stage_id
                    },
                "select":[
                "STAGE_ID",
                "CATEGORY_ID",
                "ID",
                "TITLE",
                "OPPORTUNITY",
                "CONTACT_ID",
                "UF_CRM_1729668396"
                    ]
            }
        )
        return [Deal(**deal) for deal in answ]

    def get_deal(self,id):
        logger.info("request deal {id}".format(id=id))
        answ = self.bx24.callMethod(
            method="crm.deal.get",
            params={
                "id":id
            }
        )
        return Deal(**answ)
    
    def get_contact(self,id):
        logger.info("request contact {id}".format(id=id))
        answ = self.bx24.callMethod(
            method="crm.contact.get",
            params={
                "id":id
            }
        )
        return Contact(**answ)

    def get_contacts(self,contacts_id):
        logger.info("request {contacts_count} contacts".format(contacts_count=len(contacts_id)))
        answ = self.bx24.callMethod(
            method="crm.contact.list",
            params={
                "filter":{"ID":contacts_id},
                "select":[
                    "NAME",
                    "LAST_NAME",
                    "SECOND_NAME",
                    "PHONE",
                    "UF_CRM_1729781383"
                    ]
            }
        )
        return [Contact(**contact) for contact in answ]