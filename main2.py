import logging
import asyncio
from slixmpp import ClientXMPP

class EchoBot(ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()
        print("Бот в сети! Можно писать на admin@10.0.0.12")

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            msg.reply(f"Эхо: {msg['body']}").send()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
    # Проверь, что тут твой IP
    xmpp = EchoBot('admin@10.0.0.12', 'password')
    
    # Вот тут самая важная часть для работы в новых версиях:
    xmpp.connect()
    xmpp.process(forever=True)
