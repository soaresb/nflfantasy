import requests
from bs4 import BeautifulSoup
import re
from WebScraper import WebScraper
from helpers import headers
from models.Player import Player


class FantasyProsScraper(WebScraper):
    def __init__(self, config):
        super(FantasyProsScraper, self).__init__(config)
        pass

    def is_valid_row(self, player_row):
        class_name = player_row.attrs.get("class")
        for partial in class_name:
            if re.search(r'mpb-player', partial, re.IGNORECASE):
                return True
        return False

    def scrape(self):
        players = list()
        response = requests.get(self.config.get("site"), headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup:
            tbody = soup.find("tbody")
            if tbody:
                player_rows = tbody.find_all("tr")
                if player_rows:
                    for player_row in player_rows:
                        if self.is_valid_row(player_row):
                            player = self.update_player(player_row)
                            players.append(player)
                    self.storage.bulk_update([self.storage.update_player(player) for player in players], "players")
    
    def get_fantasy_pros_id(self, player_row):
        class_name = player_row.attrs.get("class")
        for partial in class_name:
            if re.search(r'mpb-player', partial, re.IGNORECASE):
                return re.sub(r'mpb-player-', "", partial, re.IGNORECASE)
    
    def update_player(self, player_row):
        name = player_row.find("span", {"class": "full-name"}).text
        fantasy_pros_id = self.get_fantasy_pros_id(player_row)
        player = Player()
        player.load_from_dict(self.storage.fetch_one("players", {"name": name}, {"_id": 1}))
        if self.config.get("type") == "position":
            player.fantasy_pros_position_rank = int(player_row.find("td", {"class": "sticky-cell"}).text)
        else:
            player.fantasy_pros_rank = int(player_row.find("td", {"class": "sticky-cell"}).text)
        player.fantasy_pros_id = fantasy_pros_id
        return player

    