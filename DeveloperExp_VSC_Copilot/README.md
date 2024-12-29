# Development and Release Category Health Analyzer

This application analyzes the "development and release category" health of a software engineering department based on various parameters.

## Categories and Parameters

The categories and parameters are defined in the `config/categories.json` file.

## Generating Synthetic Data

To generate synthetic data, run the following command:

```bash
python src/data_generator.py
```

This will create a `data/synthetic_data.json` file with synthetic data for 15 teams.

## Analyzing Team Performance

To analyze the team performance and determine the maturity level, run the following command:

```bash
python src/analyzer.py
```

This will create a `data/maturity_levels.json` file with the maturity levels of each team.

## Adding New Categories and Parameters

To add new categories and parameters, update the `config/categories.json` file accordingly.
