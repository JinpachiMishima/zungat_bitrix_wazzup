from requests import post, get

from api.wz.wz_channel import Channel
from api.wz.message import Message

class WZ:
    def __init__(self,token):
        self.header = {
            "Authorization":f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.basic_url = "https://api.wazzup24.com/v3/"
    
    def send_message(self,message:Message):
        answ =  post(
            url="https://api.wazzup24.com/v3/message",
            headers=self.header,
            json=message.dict(by_alias=True)
        ).json()

        return answ
        

    def get_channels(self):
        answ = get(
            url=self.basic_url + "channels",
            headers=self.header
        ).json()
        return [Channel(**channel) for channel in answ]

