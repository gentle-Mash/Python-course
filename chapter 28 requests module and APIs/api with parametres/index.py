import requests
import datetime

parametres = {
    "lat":40.463669,
    "lng":-3.749220,
    "formatted":0,
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parametres)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time = datetime.datetime.now()
print(time)