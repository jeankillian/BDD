import peewee
import datetime
from models import *
msg_date = datetime.datetime.now()
print(msg_date)
# game = GameServers.create(ip_address="10.10.10.4", name="tutu", game_installed="puissance 4")
game, created = GameServers.get_or_create(ip_address="10.10.10.5", name="tuto", game_installed="puissance 4")
msg = ReceivedMessage.get_or_create(message_date=msg_date, message="coucou", message_id="1", message_machine_id="1")
