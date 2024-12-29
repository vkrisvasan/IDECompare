import streamlit as st
from modules import weather #, commute, power, holiday, events, technology, news, market, government
from config import API_CONFIG
import feedback

def main():
    st.title("My Daily Planner")

    location = st.text_input("Enter your location:")
    if location:
        weather_info = weather.get_weather(API_CONFIG["weather"], location)
        commute_info = commute.get_commute(API_CONFIG["commute"])
        power_info = power.get_power(API_CONFIG["power"])
        holiday_info = holiday.get_holiday(API_CONFIG["holiday"])
        events_info = events.get_events(API_CONFIG["events"])
        technology_info = technology.get_technology(API_CONFIG["technology"])
        news_info = news.get_news(API_CONFIG["news"])
        st.write(commute_info)
        # ...display other information...

if __name__ == "__main__":
    main()
    st.write(commute_info)
    feedback.get_feedback()

    st.subheader("Power Availability")
    st.write(power_info)
    st.write(holiday_info)
    st.subheader("Special Events")
    st.write(events_info)
    st.subheader("Technology and Research")
    st.write(technology_info)
    st.subheader("Trending News")
    st.write(news_info)
    st.subheader("Market Movements")
    st.write(market_info)
    st.subheader("Government Regulations")
    st.write(government_info)

if __name__ == "__main__":
    main()
    st.subheader("Holiday Impact")