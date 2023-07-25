import requests
import os

# here i've made a environment variable for my api key by going to terminal then write "export VARIABLE_NAME=pass the value without giving any spaces after your variable name"

KEY = os.environ.get("API_KEY")
LAT = 23.7662
LONG = 90.3589
parametres = {"lat" : LAT,
              "lon" : LONG,
              "appid" : KEY}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parametres)
response.raise_for_status()
data = response.json()

tomorrow_data = data["list"][1:10]
# print(tomorrow_data[0]["weather"][0]["id"])

weather_conditions_id = [tomorrow_data[i]["weather"][0]["id"] for i in range(len(tomorrow_data))]

# print(weather_conditions_id)

will_rain = False
for i in weather_conditions_id:
    if int(i) < 600:
        will_rain = True
if will_rain:
    print("Bring an Umbrella!!!")