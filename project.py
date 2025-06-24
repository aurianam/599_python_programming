## Premise: Indivuals with chronic conditions can be extremly sensitive to pressure changes. While most people might not
#notice a cloudy day at all, someone with an auto immune disease might be experiencing pain or other symptoms
## Additionally, you cannot tell if pressure is going to change on most weather forecasts. Just because it will be cloudy
#does not necessarily mean there will be a significant pressure change. 

##However, if individuals with these conditions were notified ahead of time they would be able to better prepare

##The following script allows a user to input their city and find out if there will be serious pressure changes in the next day

##dr sprint- this code is running- however, i had to use copilot AI to help me with some parts (which i have noted below)
#so i would still like to review what i currently have with you :)

import requests
from datetime import datetime, timedelta

# Prompt user for city
city = input("Enter your city: ")

# Geocoding request to get latitude and longitude
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_resp = requests.get(geo_url).json()

if not geo_resp.get("results"):
    print("City not found. Try a more specific name.")
    exit()

location = geo_resp["results"][0]
latitude = location["latitude"]
longitude = location["longitude"]
print(f"Location found: {location['name']}, {location.get('country', '')}")

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

#i asked copilot how to do this but i dont understand it at all 
start_index = next(i for i, t in enumerate(times) if parse_time(t) >= now)
end_index = next(i for i, t in enumerate(times) if parse_time(t) >= future)

pressures_next_24 = pressures[start_index:end_index+1]
pressure_drop = pressures_next_24[0] - min(pressures_next_24)

# Report result
print(f"\n Forecasted pressure drop in next 24 hrs: {pressure_drop:.2f} hPa")
if pressure_drop >= 5:
    print("Significant drop detected — may affect sensitive individuals.")
else:
    print("No major pressure changes expected.")