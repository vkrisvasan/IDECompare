from models.team import Team
from utils.utils import generate_synthetic_metric_value

def generate_team_data(team_names, categories_config):
    teams = []
    for team_name in team_names:
        team = Team(team_name)
        for category in categories_config["categories"]:
            for parameter in category["parameters"]:
                for metric in parameter["metrics"]:
                    team.add_data(metric, generate_synthetic_metric_value(metric))
        teams.append(team)
    return teams 