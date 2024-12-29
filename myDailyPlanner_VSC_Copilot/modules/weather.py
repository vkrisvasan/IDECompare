import requests

def get_weather(config, location):
    params = config["params"]
    params["q"] = location
    response = requests.get(config["url"], params=params, headers={"key": config["key"]})
    return response.json()
