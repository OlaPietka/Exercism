REVERSE = {'win':'loss', 'loss':'win', 'draw':'draw'}
FORMAT = '{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'


def tally(rows):
    scores = {}

    def update_points(team, res):
        score = scores.get(team, {'Team': team, "MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
        score['MP'] += 1
        score['W'] += int(res == 'win')
        score['D'] += int(res == 'draw')
        score['L'] += int(res == 'loss')
        score['P'] += 3 * int(res == 'win') + int(res == 'draw')
        scores[team] = score

    for battle in [row.split(';') for row in rows]:
        team1, team2, res = battle
        update_points(team1, res)
        update_points(team2, REVERSE[res])

    table = [FORMAT.format('Team', 'MP', 'W', 'D', 'L', 'P')]
    for t in sorted(sorted(scores.values(), key=lambda s: s['Team']), key=lambda r: r['P'], reverse=True):
        table.append(FORMAT.format(t['Team'], t['MP'], t['W'], t['D'], t['L'], t['P']))
    return table