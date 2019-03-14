import os
import json
import datetime
from models import *

class JsonAnalyser:

    def __init__(self, json_formated_string):
        data_dict = json.loads(json_formated_string)
        self.message = json_formated_string
        self.message_id = data_dict['Msg ID']
        self.name = data_dict['Machine name']
        self.game_installed = data_dict['Game type']
        self.start_date = datetime.datetime.strptime(data_dict['Start time'], "%d/%m/%y %H:%M")
        self.end_date = datetime.datetime.strptime(data_dict['End time'], "%d/%m/%y %H:%M")
        self.winner = data_dict['Winner']
        self.day = datetime.datetime.strptime(data_dict['Start time'], "%d/%m/%y %H:%M").date()
        self.machine = GameServers.get(GameServers.name == data_dict['Machine name'])
        self.game_timer = self.get_game_duration()

    def get_day(self):
        return self.day

    def get_game_duration(self):
        delta_time = self.end_date - self.start_date
        return delta_time.total_seconds()

    def get_winner(self):
        return self.winner


game, created = GameServers.get_or_create(ip_address="100.100.100.45", name="A", game_installed="puissance4")
game, created = GameServers.get_or_create(ip_address="100.100.100.78", name="B", game_installed="morpion")

test = JsonAnalyser("""{
    "Msg type": "STATS",
    "Msg ID": 235,
    "Machine name": "A",
    "Game type" : 1,
    "Start time": "26/02/19 12:22",
    "End time": "26/02/19 12:24",
    "Winner": "player1"
}""")
print(test.get_winner())

msg = ReceivedMessage.get_or_create(message=test.message, message_id=test.message_id,
                                    message_machine=test.machine)
stats_match = StatsPerMatch.get_or_create(which_machine_id=test.machine, start_date=test.start_date,
                                          game_timer=test.game_timer, winner=test.winner)
print(test.game_timer)

# stats_day = StatsPerDay.get_or_create(date_of_day=my_date, machine=game, nb_of_game="12", avg_game_timer="18",
#                                       p1_win="4", p2_win="8", player_draw="0")

