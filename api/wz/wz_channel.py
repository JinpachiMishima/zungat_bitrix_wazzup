from typing import Optional
from pydantic import Field

from api.wz.base_model import BaseConfigModel


class Channel(BaseConfigModel):
    channel_id:Optional[str] = Field(None,alias="channelId")
    transport:Optional[str] = Field(None,alias="transport")
    state:Optional[str] = Field(None,alias="state")
    plain_id:Optional[str] = Field(None,alias="plainId")
    name:Optional[str] = Field(None,alias="name")