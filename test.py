# from models import *
my_date = datetime.datetime.strptime("13/03/19 12:58", "%d/%m/%y %H:%M").date()
my_date_time = datetime.datetime.strptime("13/03/19 12:58", "%d/%m/%y %H:%M")

game, created = GameServers.get_or_create(ip_address="100.100.100.2", name="titi", game_installed="puissance 4")
msg = ReceivedMessage.get_or_create(message="coucou 1", message_id="1",
                                    message_machine_id=game)
stats_day = StatsPerDay.get_or_create(date_of_day=my_date, machine=game, nb_of_game="12", avg_game_timer="18",
                                      p1_win="4", p2_win="8", player_draw="0")
stats_match = StatsPerMatch.get_or_create(which_machine_id=game, start_date=my_date, game_timer="455",
                                          winner="player 2")
