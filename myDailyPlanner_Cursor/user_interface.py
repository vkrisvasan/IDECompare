# user_interface.py
import streamlit as st
from data_processor import DataProcessor
from planner import Planner
import config

def main():
    st.title("Your Daily Planner")

    # User input
    location = st.text_input("Enter your location:", config.DEFAULT_LOCATION)
    country = st.text_input("Enter your country:", config.DEFAULT_COUNTRY)
    category = st.text_input("Enter news category:", config.DEFAULT_CATEGORY)
    language = st.text_input("Enter language:", config.DEFAULT_LANGUAGE)
    scholar_query = st.text_input("Enter technology and research query:", "Artificial Intelligence")
    finance_query = st.text_input("Enter market query:", "stock market")

    if st.button("Generate Plan"):
        data_processor = DataProcessor()
        weather_data = data_processor.get_weather_data(location)
        news_data = data_processor.get_news_data(category, country, language)
        events_data = data_processor.get_events_data(location)
        scholar_data = data_processor.get_scholar_data(scholar_query)
        finance_data = data_processor.get_finance_data(finance_query)
        trending_news = data_processor.get_trending_news(country, language)

        planner = Planner()
        plan = planner.create_plan(weather_data, news_data, events_data, scholar_data, finance_data, trending_news)

        st.markdown(plan)

if __name__ == "__main__":
    main()