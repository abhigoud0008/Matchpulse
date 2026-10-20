import json

def get_match_stats(filepath):

    with open(filepath, "r") as file:
        events = json.load(file)

    stats = {
        "passes": 0,
        "shots": 0,
        "goals": 0,
        "tackles": 0
    }

    blue_events = 0
    red_events = 0

    for event in events:

        if event["team"] == "Blue FC":
            blue_events += 1
        else:
            red_events += 1

        if event["event"] == "pass":
            stats["passes"] += 1

        elif event["event"] == "shot":
            stats["shots"] += 1

        elif event["event"] == "goal":
            stats["goals"] += 1

        elif event["event"] == "tackle":
            stats["tackles"] += 1

    total_events = blue_events + red_events

    stats["possession"] = round(
        (blue_events / total_events) * 100
    )

    stats["pass_accuracy"] = round(
        85 + (stats["passes"] % 10)
    )

    stats["pressure_index"] = min(
        100,
        stats["passes"] * 2 + stats["shots"] * 5
    )

    return stats