from typing import Optional
from pydantic import Field

from api.wz.base_model import BaseConfigModel

class Message(BaseConfigModel):
    channel_id:Optional[str] = Field(None,alias="channelId")
    chat_type:Optional[str] = Field(None,alias="chatType")
    chat_id:Optional[str] = Field(None,alias="chatId")
    text:Optional[str] = Field(None,alias="text")
