

class GameStats(object):
    def __init__(self):
        super().__init__()
        self.game_id = None
        self.playerid = None
        self.home = None
        self.team = None
        self.passing_att = None
        self.passing_cmp = None
        self.passing_yds = None
        self.passing_tds = None
        self.passing_ints = None
        self.passing_twopta = None
        self.passing_twoptm = None
        self.rushing_att = None
        self.rushing_yds = None
        self.rusing_lng = None
        self.rushing_twopta = None
        self.rushing_twoptm = None
        self.receiving_rec = None
        self.receiving_yds = None
        self.receiving_tds = None
        self.receiving_lng = None
        self.receiving_twopta = None
        self.receiving_twoptm = None
        self.fumbles_tot = None
        self.fumbles_rcv = None
        self.fumbles_trcv = None
        self.fumbles_yds = None
        self.fumbles_lost = None
        self.defense_tkl = None
        self.defense_ask = None
        self.defense_sk = None
        self.defense_int = None
        self.defense_ffum = None
        self.kicking_fgm = None
        self.kicking_fga = None
        self.kicking_fgyds = None
        self.kicking_totpfg = None
        self.kicking_xpmade = None
        self.kicking_xpmissed = None
        self.kicking_xpa = None
        self.kicking_xab = None
        self.kicking_xptot = None
        self.punting_pts = None
        self.punting_yds = None
        self.punting_avg = None
        self.punting_i20 = None
        self.punting_lng = None
        self.kickret_ret = None
        self.kickret_avg = None
        self.kickret_tds = None
        self.kickret_lng = None
        self.puntret_ret = None
        self.puntret_avg = None
        self.puntret_tds = None
        self.puntret_lng = None
    
    def from_nfldb_game_stats(self, game_stats):
        for key, val in game_stats.__dict__.items():
            if key == "_stats":
                continue
            try:
                setattr(self, key, val)
            except AttributeError as e:
                pass
    
    def get_insert_query_and_vals(self):
        query = "INSERT INTO game_stats ("
        values_to_insert = ()
        for key, val in self.__dict__.items():
            if val and (type(val) == str or type(val) == int):
                query += "{0}, ".format(key) 
                values_to_insert =  values_to_insert + (val,)
        query = query[:-2]
        query += ") VALUES ("
        for i in values_to_insert:
            query += "%s, "
        query = query[:-2]
        query += ")"
        query += "ON DUPLICATE KEY UPDATE game_id = {0}".format(self.game_id)
        return query, values_to_insert
