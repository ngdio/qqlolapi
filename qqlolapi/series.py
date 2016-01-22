import qqlolapi.requests
import qqlolapi.match
import qqlolapi.objects.series

def by_id(id, only_ids=False):
    data = qqlolapi.requests.call("http://apps.game.qq.com/lol/match/apis/searchSMatchList.php", params={"p0": id, "r1": "SMatchListArr"})
    matches = []
    for match in data:
        if only_ids == True:
            m = int(match['sMatchId'])
        else:
            m = qqlolapi.match.by_id(int(match['sMatchId']))
        matches.append(qqlolapi.objects.series.SeriesMatch(
            num=int(match['MatchNum']),
            match=m,
        ))
    return matches