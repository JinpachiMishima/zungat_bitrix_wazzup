from typing import Optional,List,Union

from pydantic import Field

from api.bx.base_model import BaseConfigModel

class Phone(BaseConfigModel):
    id:Optional[int] = Field(None,alias="ID")
    value_type:Optional[str] = Field(None,alias="VALUE_TYPE")
    type_id:Optional[str] = Field(None,alias="TYPE_ID")
    value:Optional[str] = Field(None,alias="VALUE")


class Contact(BaseConfigModel):
    id:Optional[int] = Field(None,alias="ID")
    first_name:Optional[str] = Field(None,alias="NAME")
    last_name:Optional[str] = Field(None,alias="LAST_NAME")
    second_name:Optional[str] = Field(None,alias="SECOND_NAME")
    phones:Optional[List[Phone]] = Field(None,alias="PHONE")
    balance:Optional[float] = Field(None,alias="UF_CRM_1729781383")

