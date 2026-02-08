import logging
from slixmpp import ClientXMPP

class EchoBot(ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        self.send_presence()
        print("Бот запущен и готов к работе!")

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            msg.reply(f"Ты написал: {msg['body']} - это имба!").send()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
    # Указываем JID (твой_ник@твой_IP) и пароль
    xmpp = EchoBot('admin@10.0.0.12', 'password') 
    xmpp.connect()
    xmpp.process(forever=True)
