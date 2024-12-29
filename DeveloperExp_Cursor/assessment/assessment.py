def assess_team_maturity(teams, categories_config):
    maturity_levels = categories_config["maturity_levels"]
    for team in teams:
        total_score = 0
        for metric, value in team.get_data().items():
            total_score += value
        average_score = total_score / len(team.get_data())

        team_maturity = "Low"
        for level, score_range in maturity_levels.items():
            if score_range["min_score"] <= average_score <= score_range["max_score"]:
                team_maturity = level
                break
        team.set_maturity_level(team_maturity)
    return teams 