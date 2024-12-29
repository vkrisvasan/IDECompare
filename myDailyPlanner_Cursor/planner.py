# planner.py
from typing import Dict, Any, List

class Planner:
    def __init__(self):
        pass

    def create_plan(self, weather_data: Dict[str, Any], news_data: List[Dict[str, Any]],
                    events_data: List[Dict[str, Any]], scholar_data: List[Dict[str, Any]],
                    finance_data: List[Dict[str, Any]], trending_news: List[Dict[str, Any]]) -> str:
        """
        Generates a daily plan based on the provided data.

        Args:
            weather_data (Dict[str, Any]): Weather data.
            news_data (List[Dict[str, Any]]): News data.
            events_data (List[Dict[str, Any]]): Events data.
            scholar_data (List[Dict[str, Any]]): Scholar data.
            finance_data (List[Dict[str, Any]]): Finance data.
            trending_news (List[Dict[str, Any]]): Trending news data.

        Returns:
            str: The generated daily plan.
        """
        plan = "## Your Daily Plan\n\n"

        # Weather
        if weather_data and "forecast" in weather_data and "forecastday" in weather_data["forecast"]:
            forecast = weather_data["forecast"]["forecastday"][0]
            plan += f"### Weather:\n"
            plan += f"- Condition: {forecast['day']['condition']['text']}\n"
            plan += f"- Temperature: {forecast['day']['avgtemp_c']}°C\n"
            plan += f"- Max Temperature: {forecast['day']['maxtemp_c']}°C\n"
            plan += f"- Min Temperature: {forecast['day']['mintemp_c']}°C\n"
            plan += f"- Chance of rain: {forecast['day']['daily_chance_of_rain']}%\n\n"
        else:
            plan += "### Weather: No weather data available.\n\n"

        # News
        if news_data:
            plan += "### News:\n"
            for article in news_data[:5]:  # Displaying top 5 articles
                plan += f"- {article['title']}: {article['description']}\n"
            plan += "\n"
        else:
            plan += "### News: No news data available.\n\n"

        # Events
        if events_data:
            plan += "### Events:\n"
            for event in events_data[:5]:
                plan += f"- {event['title']}: {event['description']}\n"
            plan += "\n"
        else:
            plan += "### Events: No events data available.\n\n"

        # Scholar
        if scholar_data:
            plan += "### Technology and Research:\n"
            for article in scholar_data[:5]:
                plan += f"- {article['title']}: {article['snippet']}\n"
            plan += "\n"
        else:
            plan += "### Technology and Research: No research data available.\n\n"

        # Finance
        if finance_data:
            plan += "### Market Movements:\n"
            for market in finance_data[:1]:
                if isinstance(market, dict):
                    plan += f"- {market.get('name', 'N/A')}: {market.get('price', 'N/A')}\n"
            plan += "\n"
        else:
            plan += "### Market Movements: No market data available.\n\n"

        # Trending News
        if trending_news:
            plan += "### Trending News:\n"
            for article in trending_news[:5]:
                plan += f"- {article['title']}: {article['description']}\n"
            plan += "\n"
        else:
            plan += "### Trending News: No trending news data available.\n\n"

        return plan