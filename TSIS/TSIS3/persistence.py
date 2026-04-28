import json
import os

def load_json(filename, default):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default, f)
        return default
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def update_leaderboard(name, score):
    scores = load_json('leaderboard.json', [])
    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]
    save_json('leaderboard.json', scores)