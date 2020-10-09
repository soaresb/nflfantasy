import time
import uvicorn
from lib.models.mongo import database
from lib.helpers import make_response
from lib.models.mysql import BaseMySQL
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mysql = BaseMySQL(password="GOmanny1436", database="nflgame")

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.get("/player/{_id}")
def get_player_by_id(_id: int = Path(..., title="The id of the player to get.")):
    players = database.players
    player = players.find_one({"_id": int(_id)})
    return make_response(200, player)


@app.get("/player/stats/{_id}")
def get_player_stats_by_id(_id: str = Path(..., title="The id of the player to get.")):
    columns, player_stats = mysql.execute_query("SELECT * FROM game_stats WHERE playerid = %s", (_id,))
    data = dict(zip(columns, player_stats))
    return make_response(200, "stats")


@app.get("/player/{name}")
def get_player_by_name(name: str = Path(..., title="The name of the player to get.")):
    players = database.players
    player = players.find_one({"name": {"$regex": name}})
    return make_response(200, player)

@app.get("/players")
def get_players(team: Optional[str] = None, position: Optional[str]= None, sort: Optional[str] = None):
    query = {}
    if team and team != "ALL":
        if not query.get("$and"):
            query["$and"] = []
        query["$and"].append({"team": {"$in": team.split(",")}})
    if position and position != "ALL":
        if not query.get("$and"):
            query["$and"] = []
        query["$and"].append({"position": {"$in": position.split(",")}})
    if sort:
        if sort == "player":
            query["fantasy_pros_position_rank"] = {"$exists": True, "$ne": None}
            players = database.players.find(query).sort("fantasy_pros_position_rank").limit(50)
        elif sort == "all":
            query["fantasy_pros_rank"] = {"$exists": True, "$ne": None}
            players = database.players.find(query).sort("fantasy_pros_rank").limit(50)
        else:
            players = database.players.find(query).limit(50)
    else:
        players = database.players.find(query).limit(50)
    return make_response(200, list(players))

@app.route("/players/team/<string:team>")
def get_players_by_team(team):
    players = list(database.players.find({"team": {"$regex": team}}))
    return make_response(200, players)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)