import requests
import json
from typing import Dict, Any

class APIClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def get(self, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Sends a GET request to the specified URL with optional parameters.

        Args:
            url (str): The URL to send the request to.
            params (Dict[str, Any], optional): The parameters to include in the request. Defaults to None.

        Returns:
            Dict[str, Any]: The JSON response from the API, or an empty dictionary if an error occurs.
        """
        headers = {}
        if self.api_key:
            params = params or {}
            params["api_key"] = self.api_key
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return {}
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            return {}
