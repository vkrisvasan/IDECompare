# data_processor.py
from typing import Dict, Any, List
from api_client import APIClient
import config

class DataProcessor:
    def __init__(self):
        self.weather_client = APIClient(config.WEATHER_API_KEY)
        self.news_client = APIClient(config.NEWS_API_KEY)
        self.serpapi_client = APIClient(config.SERPAPI_KEY)
        self.newsdata_client = APIClient(config.NEWS_DATA_API_KEY)

    def get_weather_data(self, location: str) -> Dict[str, Any]:
        """
        Fetches weather data for a given location.

        Args:
            location (str): The location to fetch weather data for.

        Returns:
            Dict[str, Any]: The weather data, or an empty dictionary if an error occurs.
        """
        params = {
            "q": location,
            "days": 1,
            "aqi": "no",
            "alerts": "no"
        }
        return self.weather_client.get(config.WEATHER_API_URL, params=params)

    def get_news_data(self, category: str, country: str, language: str) -> List[Dict[str, Any]]:
        """
        Fetches news data for a given category, country, and language.

        Args:
            category (str): The category of news to fetch.
            country (str): The country to fetch news from.
            language (str): The language of the news to fetch.

        Returns:
            List[Dict[str, Any]]: A list of news articles, or an empty list if an error occurs.
        """
        params = {
            "category": category,
            "country": country,
            "language": language
        }
        news_data = self.news_client.get(config.NEWS_API_URL, params=params)
        return news_data.get("articles", [])

    def get_events_data(self, location: str) -> List[Dict[str, Any]]:
        """
        Fetches events data for a given location.

        Args:
            location (str): The location to fetch events data for.

        Returns:
            List[Dict[str, Any]]: A list of events, or an empty list if an error occurs.
        """
        params = {
            "q": f"events in {location}",
        }
        events_data = self.serpapi_client.get(config.GOOGLE_EVENTS_API_URL, params=params)
        return events_data.get("events_results", [])

    def get_scholar_data(self, query: str) -> List[Dict[str, Any]]:
        """
        Fetches scholar data for a given query.

        Args:
            query (str): The query to fetch scholar data for.

        Returns:
            List[Dict[str, Any]]: A list of scholar results, or an empty list if an error occurs.
        """
        params = {
            "q": query,
        }
        scholar_data = self.serpapi_client.get(config.GOOGLE_SCHOLAR_API_URL, params=params)
        return scholar_data.get("organic_results", [])

    def get_finance_data(self, query: str) -> List[Dict[str, Any]]:
        """
        Fetches finance data for a given query.

        Args:
            query (str): The query to fetch finance data for.

        Returns:
            List[Dict[str, Any]]: A list of finance results, or an empty list if an error occurs.
        """
        params = {
            "q": query,
        }
        finance_data = self.serpapi_client.get(config.GOOGLE_FINANCE_API_URL, params=params)
        return finance_data.get("markets", [])

    def get_trending_news(self, country: str, language: str) -> List[Dict[str, Any]]:
        """
        Fetches trending news data for a given country and language.

        Args:
            country (str): The country to fetch news from.
            language (str): The language of the news to fetch.

        Returns:
            List[Dict[str, Any]]: A list of news articles, or an empty list if an error occurs.
        """
        params = {
            "country": country,
            "language": language,
        }
        news_data = self.newsdata_client.get(config.NEWS_DATA_API_URL, params=params)
        return news_data.get("results", [])