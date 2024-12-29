from data_generator.data_generator import generate_team_data
from assessment.assessment import assess_team_maturity
from utils.utils import load_config

if __name__ == "__main__":
    config_path = "config/categories.json"
    categories_config = load_config(config_path)

    team_names = [f"Team {i}" for i in range(1, 16)]
    teams = generate_team_data(team_names, categories_config)
    teams = assess_team_maturity(teams, categories_config)

    for team in teams:
        print(team) 