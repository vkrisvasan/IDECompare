"""
ChatGPT
Prompt 1: generate an application to understand the "development and release category" health of a software engineering department looking at the following parameters in the category (a) codebase health (b) development environment i.e developer tools and ci/cd tools for pipeline (c) automated testing health i.e test coverage, test environment, test data setup and (d) frictionless release health. the application should generate synthetic data of jira, git, sonar, semgrep, snyk, developer survey, DORA metrics for as is state analysis for 15 different teams and be able to say which maturity level [Elite, High, Medium, low] each team is based on the parameters within the category. Write the application in a modular, loosely couple way. it is good practice to keep the category and the parameters outside of the python code in a file and build feature in code to encourage addition of new category and parameters.
"""

import json
import random
import pandas as pd
from typing import List, Dict

class MaturityAnalysis:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)

    @staticmethod
    def load_config(config_file: str) -> Dict:
        """Load category and parameter definitions from JSON file."""
        with open(config_file, "r") as file:
            return json.load(file)

    def fetch_synthetic_metrics(self, teams: List[str]) -> pd.DataFrame:
        """Fetch synthetic metrics from various sources."""
        data = []
        for team in teams:
            team_data = {"Team": team}

            # Simulated Jira Metrics
            team_data["jira_issues_resolved"] = random.randint(70, 100)  # Issue resolution rate
            team_data["jira_scope_creep"] = random.randint(0, 20)  # Lower is better

            # Simulated Git Metrics
            team_data["git_merge_conflicts"] = random.randint(0, 20)  # Lower is better
            team_data["git_commit_frequency"] = random.randint(50, 150)  # Higher is better

            # Simulated SonarQube Metrics
            team_data["sonar_code_smells"] = random.randint(0, 100)  # Lower is better
            team_data["sonar_coverage"] = random.randint(50, 95)  # Test coverage percentage

            # Simulated Semgrep Metrics
            team_data["semgrep_issues"] = random.randint(0, 50)  # Security issues count

            # Simulated Snyk Metrics
            team_data["snyk_vulnerabilities"] = random.randint(0, 50)  # Vulnerabilities count

            # Simulated Developer Survey
            team_data["developer_tool_satisfaction"] = random.randint(50, 100)  # Developer satisfaction

            # Simulated DORA Metrics
            team_data["dora_deployment_frequency"] = random.choice(["Elite", "High", "Medium", "Low"])
            team_data["dora_lead_time"] = random.choice(["Elite", "High", "Medium", "Low"])
            team_data["dora_change_failure_rate"] = random.choice(["Elite", "High", "Medium", "Low"])
            team_data["dora_time_to_restore"] = random.choice(["Elite", "High", "Medium", "Low"])

            # Normalize metrics to match the parameter names in configuration
            team_data["codebase_health"] = 100 - team_data["sonar_code_smells"]
            team_data["developer_tools"] = team_data["developer_tool_satisfaction"]
            team_data["automated_testing_health"] = team_data["sonar_coverage"]
            team_data["frictionless_release"] = 100 - (
                team_data["git_merge_conflicts"] + team_data["jira_scope_creep"]
            )

            data.append(team_data)
        return pd.DataFrame(data)

    @staticmethod
    def calculate_maturity(data: pd.DataFrame, thresholds: Dict) -> pd.DataFrame:
        """Calculate maturity level for each team based on thresholds."""
        data["Overall Score"] = data.iloc[:, 1:].mean(axis=1)
        data["Maturity Level"] = data["Overall Score"].apply(
            lambda score: next(
                (level for level, threshold in thresholds.items() if score >= threshold),
                "Low"
            )
        )
        return data

    def analyze_category(self, category_name: str, teams: List[str]) -> pd.DataFrame:
        """Perform maturity analysis for a specific category."""
        category = self.config.get(category_name)
        if not category:
            raise ValueError(f"Category '{category_name}' not found in configuration.")

        parameters = category["parameters"].keys()
        thresholds = category["thresholds"]

        # Fetch synthetic metrics
        data = self.fetch_synthetic_metrics(teams)

        # Calculate maturity
        result = self.calculate_maturity(data[list(parameters)], thresholds)
        return result


def main():
    # Initialize with configuration file
    config_file = "categories.json"
    analyzer = MaturityAnalysis(config_file)

    # Define teams
    teams = [f"Team {i+1}" for i in range(15)]

    # Analyze "Development and Release" category
    category_name = "Development and Release"
    analysis_result = analyzer.analyze_category(category_name, teams)

    # Display the result
    print("Maturity Analysis Result:")
    print(analysis_result)

    # Save the result to CSV
    analysis_result.to_csv(f"{category_name.replace(' ', '_').lower()}_maturity.csv", index=False)
    print(f"Results saved to {category_name.replace(' ', '_').lower()}_maturity.csv")


if __name__ == "__main__":
    main()
