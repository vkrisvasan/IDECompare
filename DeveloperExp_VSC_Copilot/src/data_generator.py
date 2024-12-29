import random
import json
import os

def generate_synthetic_data():
    teams = [f"Team_{i}" for i in range(1, 16)]
    data = {}

    for team in teams:
        data[team] = {
            "jira": random.randint(50, 100),
            "git": random.randint(50, 100),
            "sonar": random.randint(50, 100),
            "semgrep": random.randint(50, 100),
            "snyk": random.randint(50, 100),
            "developer_survey": random.randint(50, 100),
            "dora_metrics": random.randint(50, 100)
        }

    return data

if __name__ == "__main__":
    synthetic_data = generate_synthetic_data()

    output_dir = "../data"
    output_file = os.path.join(output_dir, "synthetic_data.json")
    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    with open("../data/synthetic_data.json", "w") as f:
        json.dump(synthetic_data, f, indent=4)
