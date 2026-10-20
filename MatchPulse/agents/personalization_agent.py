def analyst_view(stats):

    return f"""
Possession : {stats['possession']}%
Pass Accuracy : {stats['pass_accuracy']}%
Goals : {stats['goals']}
Shots : {stats['shots']}
Pressure Index : {stats['pressure_index']}
"""


def fan_view():

    return """
Blue FC is dominating the match and
creating more chances than Red FC.
"""


def player_view():

    return """
⭐ Player Spotlight

Alex

Goals : 1
Shots : 2
Key Contribution :
Scored the winning goal.
"""


def studio_view():

    return """
📺 Broadcast Insight

8-pass build-up before goal.

Recommended Display Duration:
8 Seconds
"""
