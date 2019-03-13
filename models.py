from peewee import *
import datetime
import jsondata

mysql_db = MySQLDatabase('GAME', user='killian', password='Grimmjow26', host='localhost', port=3306)
mysql_db.connect()


class GameServers(Model):
    ip_address = CharField(unique=True)
    name = CharField(unique=True, max_length=100)
    game_installed = CharField(max_length=45)

    class Meta:
        database = mysql_db

    @classmethod
    def list_of_servers(cls):
        table = []
        for object in GameServers.select(GameServers):
            recup = [object.ip_address, object.name, object.game_installed]
            table.append(recup)
        return table


class ReceivedMessage(Model):
    message = CharField(max_length=1000)
    message_id = IntegerField()
    message_date = DateTimeField(default=datetime.datetime.now)
    message_machine = ForeignKeyField(GameServers, backref='ReceivedMessage')

    class Meta:
        database = mysql_db

    @classmethod
    def list_of_message(cls, machine):
        return ReceivedMessage.select().where(ReceivedMessage.message_machine == machine).\
            order_by(ReceivedMessage.message_date)


class StatsPerMatch(Model):
    which_machine = ForeignKeyField(GameServers, backref='StatsPerMatch')
    start_date = DateTimeField()
    game_timer = IntegerField()
    winner = CharField(max_length=100)

    class Meta:
        database = mysql_db


class StatsPerDay(Model):
    date_of_day = DateField()
    machine = ForeignKeyField(GameServers, backref='StatsPerDay')
    nb_of_game = IntegerField()
    avg_game_timer = IntegerField()
    p1_win = IntegerField()
    p2_win = IntegerField()
    player_draw = IntegerField()

    class Meta:
        database = mysql_db


mysql_db.create_tables([GameServers, ReceivedMessage, StatsPerMatch, StatsPerDay])
print(GameServers.list_of_servers())
