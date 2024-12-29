import streamlit as st
import requests
import json
from datetime import datetime

# Load API configurations
from config import API_CONFIG

def fetch_weather():
    url = f"{API_CONFIG['weather_api']['url']}?q={API_CONFIG['location']}&appid={API_CONFIG['weather_api']['key']}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_news(category):
    url = f"{API_CONFIG['news_api']['url']}"
    params = {
        'apikey': API_CONFIG['news_api']['key'],
        'q': category,
        'qInTitle': API_CONFIG['location'] # Use location for news relevance
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_events():
    url = f"{API_CONFIG['events_api']['url']}?key={API_CONFIG['events_api']['key']}&location={API_CONFIG['location']}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Hello KV")
        print(response.json())
        return response.json()
    return None

def fetch_scholar_articles():
    url = f"{API_CONFIG['scholar_api']['url']}?key={API_CONFIG['scholar_api']['key']}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_market_data():
    url = f"{API_CONFIG['finance_api']['url']}?key={API_CONFIG['finance_api']['key']}"
    response = requests.get(url)
    if response.status_code == 200:
        market_data = response.json()
        indian_market = [m for m in market_data.get('markets', []) if 'India' in m.get('name', '')]
        us_market = [m for m in market_data.get('markets', []) if 'US' in m.get('name', '')]
        return {'Indian Market': indian_market, 'US Market': us_market}
    return None

def display_plan(weather, news, events, articles, market):
    st.title("Your Daily Plan")

    st.header("Weather Forecast")
    if weather:
        st.write(f"Location: {API_CONFIG['location']}")
        st.write(f"Condition: {weather['weather'][0]['description'].capitalize()}")
        st.write(f"Temperature: {weather['main']['temp']} °C")
    else:
        st.write("Unable to fetch weather data.")

    st.header("Commute and Travel News")
    if news:
        for article in news.get('articles', [])[:5]:
            st.write(f"- {article['title']} ({article['source']['name']})")
    else:
        st.write("Unable to fetch news data.")

    st.header("Special Events")
    if events:
        for event in events.get('events', [])[:5]:
            st.write(f"- {event['title']} on {event['date']}")
    else:
        st.write("Unable to fetch events data.")

    st.header("Technology & Research Articles")
    if articles:
        for article in articles.get('articles', [])[:5]:
            st.write(f"- {article['title']} ({article['source']['name']})")
    else:
        st.write("Unable to fetch scholar articles.")

    st.header("Market Movements")
    if market:
        st.subheader("Indian Market")
        for market_item in market.get('Indian Market', [])[:5]:
            st.write(f"- {market_item['name']}: {market_item['value']}")
        st.subheader("US Market")
        for market_item in market.get('US Market', [])[:5]:
            st.write(f"- {market_item['name']}: {market_item['value']}")
    else:
        st.write("Unable to fetch market data.")

# Streamlit UI
st.sidebar.title("Daily Planner Settings")
API_CONFIG['location'] = st.sidebar.text_input("Enter your location:", API_CONFIG['location'])

if st.sidebar.button("Generate Plan"):
    weather_data = fetch_weather()
    news_data = fetch_news("commute")
    events_data = ""
    scholar_articles = ""
    market_data = ""

    events_data = fetch_events()
    #scholar_articles = fetch_scholar_articles()
    #market_data = fetch_market_data()

    display_plan(weather_data, news_data, events_data, scholar_articles, market_data)

# Feedback Section
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Share your feedback about today's plan:")
if st.sidebar.button("Submit Feedback"):
    with open("feedback.txt", "a") as f:
        f.write(f"{datetime.now()}: {feedback}\n")
    st.sidebar.success("Thank you for your feedback!")