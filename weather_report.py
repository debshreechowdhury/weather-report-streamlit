import requests
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd 

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": st.session_state.cityname,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info from the data
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    visibility = data["visibility"]
    pressure = data["main"]["pressure"]
    description = data["weather"][0]["description"]
    
    # 6. Store the city's weather details in session state
    st.session_state.city_weather_details = f"In {city_name}, it is {temp}°C, humidity {humidity}, wind speed {wind_speed}, visibility {visibility}, and pressure {pressure}  with {description}."
    st.session_state.city_temp_details = {
        "Min Temperature": data["main"]["temp_min"],
        "Current Temperature": data["main"]["temp"],
        "Max Temperature": data["main"]["temp_max"],
        "Feels like Temperature": data["main"]["feels_like"]
        }

if "city_weather_details" not in st.session_state:
    st.session_state.city_weather_details = ""

if "city_temp_details" not in st.session_state:
    st.session_state.city_temp_details = ""

st.title("Weather Report Streamlit App")
st.text_input("Please enter the name of a city:", key="cityname", on_change=get_weather)
st.button("Get Weather Information", on_click=get_weather)
st.write(st.session_state.city_weather_details)
if st.session_state.city_temp_details:
    df = pd.DataFrame(list(st.session_state.city_temp_details.items()), columns=["Temperature Type", "Temperature (Celsius)"])
    st.subheader("Temperature Analysis")
    st.bar_chart(
        df,
        x="Temperature Type",
        y="Temperature (Celsius)",
        x_label="Temperature Type",
        y_label="Temperature (Celsius)"
    )
