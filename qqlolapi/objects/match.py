class Player:
    def __init__(self, id, name, role, champion, spells, items, kills, deaths, assists, cs, gold, extra_fields=False):
        self.id = id
        self.name = name
        self.role = role
        self.champion = champion
        self.spells = spells
        self.items = items
        self.trinket = self.items[6]
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.cs = cs
        self.gold = gold
        if extra_fields == True:
            self.spell1 = self.spells[0]
            self.spell2 = self.spells[1]
            self.item1 = self.items[0]
            self.item2 = self.items[1]
            self.item3 = self.items[2]
            self.item4 = self.items[3]
            self.item5 = self.items[4]
            self.item6 = self.items[5]
            self.item7 = self.items[6]
    def __str__(self):
        return self.name

class Team:
    def __init__(self, id, name, side, winner, bans, dragon_kills, baron_kills, tower_kills, extra_fields=False):
        self.id = id
        self.name = name
        self.side = side
        self.winner = winner
        self.bans = bans
        self.dragon_kills = dragon_kills
        self.baron_kills = baron_kills
        self.tower_kills = tower_kills
        self.players = []
        if extra_fields == True:
            self.ban1 = bans[0]
            self.ban2 = bans[1]
            self.ban3 = bans[2]
    def add_player(self, new_player):
        self.players.append(new_player)
    def _player_stats(self, attr):
        stat = 0
        for x in self.players:
            stat += getattr(x, attr)
        return stat    
    def kills(self):
        return self._player_stats("kills")
    def deaths(self):
        return self._player_stats("deaths")
    def gold(self):
        return self._player_stats("gold")
    def cs(self):
        return self._player_stats("cs")
    def __str__(self):
        return self.name

class Match:
    def __init__(self, id, series_id, game_num, game_status, winner, date, left_team, right_team):
        self.id = id
        self.series_id = series_id
        self.game_num = game_num
        self.game_status = game_status
        self.winner = winner
        self.date = date
        self.left_team = left_team
        self.right_team = right_team
        self.teams = [self.left_team, self.right_team]
    def __str__(self):
        return "{} vs {}".format(self.left_team.name, self.right_team.name)