#!python
import nflgame
from storage.Mongo import Mongo
from models.GameStats import GameStats
from storage.BaseMySQL import BaseMySQL

week = 1
year = 2009

MAX_YEAR = 2020
MAX_WEEK = 17

mongo = Mongo()
mysql = BaseMySQL(password="GOmanny1436", database="nflgame")
ignore = set()
players_dict = dict()

game_stats = list()

while year < MAX_YEAR:
    games = nflgame.games(year, week=week)
    for game in games:
        players = nflgame.combine_game_stats([game])
        for player in players:
            if player.playerid in players:
                game_stat = GameStats()
                game_stat.from_nfldb_game_stats(player)
                game_stat.game_id = game.eid
                game_stats.append(game_stat)
            elif player.playerid not in ignore:
                _player = mongo.fetch_one("players", {"short_name": player.name})
                if _player:
                    players_dict[player.playerid] = _player.get("_id")
                    game_stat = GameStats()
                    game_stat.from_nfldb_game_stats(player)
                    game_stat.game_id = game.eid
                    query, values_to_insert = game_stat.get_insert_query_and_vals()
                    mysql.insert_update(query, values_to_insert)
                    game_stats.append(game_stat)
                else:
                    ignore.add(player.playerid)
                    continue
            else:
                continue

    week += 1
    if week > MAX_WEEK:
        year += 1
        week = 1



    
    
    