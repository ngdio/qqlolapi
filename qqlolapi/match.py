import json
import datetime
import pytz
import qqlolapi.requests
import qqlolapi.series
import qqlolapi.objects.match
import qqlolapi.objects.roles

def by_id(id, extra_fields=False):
    data = qqlolapi.requests.call("http://apps.game.qq.com/lol/match/apis/searchMatchInfo_s.php", params={'p0': id, 'r1': "MatchInfo"})
    matchinfo = data['sMatchInfo']
    battle = json.loads(data['battleInfo']['BattleData'])
    # Date
    date_string = "{} {}".format(battle['game-date'], battle['game-time'])
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    date = pytz.timezone("Asia/Shanghai").localize(date)
    date_utc = date.astimezone(pytz.utc)
    # Teams
    team_names = matchinfo["bMatchName"].split(" vs ")
    team_ids = {
        matchinfo["TeamA"]: team_names[0],
        matchinfo["TeamB"]: team_names[1],
    }
    ###
    match_players = {x["MemberId"]: x for x in data["sMatchMember"]}
    teams = {}
    for side in ["left", "right"]:
        tb = battle[side]
        battle_players = {x["memberId"]: x for x in tb["players"]}
        first_member = tb["players"][0]["memberId"]
        team_id = match_players[first_member]["TeamId"]
        winning_team = battle["game-win"]
        if winning_team == side:
            winner = True
        else:
            winner = False
        bans = [
            int(tb['ban-hero-1']),
            int(tb['ban-hero-2']),
            int(tb['ban-hero-3']),
        ]
        team = qqlolapi.objects.match.Team(
            id=int(team_id),
            name=team_ids[team_id],
            side=side,
            winner=winner,
            bans=bans,
            dragon_kills=int(tb['s-dragon']),
            baron_kills=int(tb['b-dragon']),
            tower_kills=int(tb['tower']),
            extra_fields=extra_fields,
        )
        for tp in tb['players']:
            p_name = tp["name"][len(team.name):]
            p_items = []
            for key, value in sorted(tp["equip"].items()):
                p_items.append(int(value))
            team.add_player(qqlolapi.objects.match.Player(
                id=int(tp["memberId"]),
                name=p_name,
                role=qqlolapi.objects.roles.ROLES_BY_ID[int(match_players[tp["memberId"]]["Place"])],
                champion=int(tp["hero"]),
                spells=[int(tp["skill-1"]), int(tp["skill-2"])],
                items=p_items,
                kills=int(tp["kill"]),
                deaths=int(tp["death"]),
                assists=int(tp["assist"]),
                cs=int(tp["lasthit"]),
                gold=int(tp["gold"]),
                extra_fields=extra_fields,
            ))
        teams[side] = team
    ###
    lteam = teams["left"]
    rteam = teams["right"]
    rmatch = qqlolapi.objects.match.Match(
        id=int(matchinfo["sMatchId"]),
        series_id=int(matchinfo["bMatchId"]),
        game_num=int(matchinfo["MatchNum"]),
        game_status=int(matchinfo["MatchStatus"]),
        winner=battle["game-win"],
        date=date_utc,
        left_team=lteam,
        right_team=rteam)
    return rmatch

def by_series(series_id, game_num, extra_fields=False):
    data = qqlolapi.series.by_id(series_id, only_ids=True)
    matches = {x.num: x for x in data}
    return by_id(int(matches[game_num].match), extra_fields=extra_fields)