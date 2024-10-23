from bitrix24 import Bitrix24

from api.bx.bx_deal import Deal
from api.bx.bx_contact import Contact

class BX:
    def __init__(self,token):
        self.token = token
        self.bx24 = Bitrix24(token)
    
    def get_deals(self,category_id,stage_id):
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
        answ = self.bx24.callMethod(
            method="crm.deal.get",
            params={
                "id":id
            }
        )
        return Deal(**answ)
    
    def get_contact(self,id):
        answ = self.bx24.callMethod(
            method="crm.contact.get",
            params={
                "id":id
            }
        )
        return Contact(**answ)

    def get_contacts(self,contacts_id):
        answ = self.bx24.callMethod(
            method="crm.contact.list",
            params={
                "filter":{"ID":contacts_id},
                "select":[
                    "name",
                    "last_name",
                    "second_name",
                    "UF_CRM_1726651117840"
                    ]
            }
        )
        return [Contact(**contact) for contact in answ]