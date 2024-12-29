API_CONFIG = {
    "weather": {
        "url": "http://api.weatherapi.com/v1/forecast.json",
        "key": "", #repalce with your key
        "params": {
            "q": "location",
            "days": 1
        }
    },
    "commute": {
        "url": "https://newsapi.org/v2/top-headlines",
        "key": "", #repalce with your key
        "params": {
            "country": "in",
            "category": "general"
        }
    },
    # ...other API configurations...
}
