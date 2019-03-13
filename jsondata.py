import os
import json

date_parties = []
for game in os.listdir('./Partie'):
    with open('./Partie/' + game, 'r') as fichier:
        date = json.loads(fichier.read())
        date_parties.append(date)
        print(date)
print(date_parties)


class DataTable:

    def __init__(self):
        print()

    def get_day(self):
        day_table = []

    def get_game_duration(self):
        game_duration_table = []

    def get_winner(self):
        winner_table = []
