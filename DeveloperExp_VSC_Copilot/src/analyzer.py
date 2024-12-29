import json

def load_categories(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def analyze_team_performance(data):
    maturity_levels = {}
    for team, metrics in data.items():
        average_score = sum(metrics.values()) / len(metrics)
        if average_score >= 85:
            maturity_levels[team] = "Elite"
        elif average_score >= 70:
            maturity_levels[team] = "High"
        elif average_score >= 50:
            maturity_levels[team] = "Medium"
        else:
            maturity_levels[team] = "Low"
    return maturity_levels

if __name__ == "__main__":
    with open("../data/synthetic_data.json", "r") as f:
        synthetic_data = json.load(f)
    
    categories = load_categories("../config/categories.json")
    maturity_levels = analyze_team_performance(synthetic_data)
    
    with open("../data/maturity_levels.json", "w") as f:
        json.dump(maturity_levels, f, indent=4)
