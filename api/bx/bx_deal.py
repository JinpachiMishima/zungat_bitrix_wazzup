from typing import Optional,List, Union

from pydantic import Field

from api.bx.base_model import BaseConfigModel

class Deal(BaseConfigModel):
    stage_id:Optional[str] = Field(None,alias="STAGE_ID")
    category_id:Optional[int] = Field(None,alias="CATEGORY_ID")
    id:Optional[int] = Field(None,alias="ID")
    title:Optional[str] = Field(None,alias="TITLE")
    opportunity:Optional[float] = Field(None,alias="OPPORTUNITY")
    client_id:Optional[int] = Field(None,alias="CONTACT_ID")
    guarantor:Union[bool,List[int]] = Field(False,alias="UF_CRM_1729668396")
