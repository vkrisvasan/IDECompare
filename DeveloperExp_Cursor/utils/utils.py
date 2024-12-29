import json
import random

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def generate_synthetic_metric_value(metric):
    if metric in ["sonar_code_smell_density", "semgrep_vulnerabilities", "snyk_vulnerabilities", "change_failure_rate"]:
        return random.uniform(0, 100) # Lower is better
    elif metric in ["developer_tool_satisfaction", "ci_cd_pipeline_efficiency", "test_coverage", "test_environment_stability", "test_data_setup_efficiency", "deployment_frequency", "lead_time_for_changes", "mean_time_to_recovery"]:
        return random.uniform(0, 100) # Higher is better
    else:
        return random.uniform(0, 100)