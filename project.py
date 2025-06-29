## Premise: Indivuals with chronic conditions can be extremly sensitive to pressure changes. While most people might not
#notice a cloudy day at all, someone with an auto immune disease might be experiencing pain or other symptoms
## Additionally, you cannot tell if pressure is going to change on most weather forecasts. Just because it will be cloudy
#does not necessarily mean there will be a significant pressure change. 

##However, if individuals with these conditions were notified ahead of time they would be able to better prepare

##The following script allows a user to input their city and find out if there will be serious pressure changes in the next day

import requests
from datetime import datetime, timedelta
import pandas

import streamlit

streamlit.title("Pressure changes check for sensitive individuals")
streamlit.write("Please type a city close to you so that we can check for pressure changes.")
city = streamlit.text_input("City: ")
# # Prompt user for city
# city = input("Enter your city: ")

# Geocoding request to get latitude and longitude
if city:
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_resp = requests.get(geo_url).json()

    if not geo_resp.get("results"):
        streamlit.error("City not found. Try a more specific name.")
   
    else:
        location = geo_resp["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        streamlit.write(f"Location found: {location['name']}, {location.get('country', '')}")

        # Build forecast API URL
        weather_url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=pressure_msl&timezone=auto")

        # Fetch forecast data
        forecast = requests.get(weather_url).json()
        times = forecast["hourly"]["time"]
        pressures = forecast["hourly"]["pressure_msl"]

        # Find pressure trend for next 24 hours
        now = datetime.now()
        future = now + timedelta(hours=24)

       
        def parse_time(t): return datetime.strptime(t, "%Y-%m-%dT%H:%M")

        press_ser = pandas.Series(data=pressures, index=pandas.to_datetime(times))
        press24_ser = press_ser[(press_ser.index > now) & (press_ser.index <= future)]
        pressure_drop = press24_ser.iloc[0] - press24_ser.min()

        # pressures_next_24 = pressures[start_index:end_index+1]
        # pressure_drop = pressures_next_24[0] - min(pressures_next_24)

        # Report result
        # print(f"\n Forecasted pressure drop in next 24 hrs: {pressure_drop:.2f} hPa")
        # if pressure_drop >= 5:
        #     print("Significant drop detected — may affect sensitive individuals.")
        # else:
        #     print("No major pressure changes expected.")
        # Report result (Streamlit-friendly)
        streamlit.write(f"**Forecasted pressure drop in next 24 hrs:** {pressure_drop:.2f} hPa")
        if pressure_drop >= 5:
            streamlit.warning("⚠️ Significant drop detected — may affect sensitive individuals.")
        else:
            streamlit.success("✅ No major pressure changes expected.")

    

