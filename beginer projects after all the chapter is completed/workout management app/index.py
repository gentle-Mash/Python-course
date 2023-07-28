import requests
from datetime import datetime

APP_ID = "bf166c26"
APP_KEY = "c47c6a252d9129ec73c53c50e2606716"

exercise_name = input("tell me which exercise you did? ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/d56279c796fcaee125aa3791536fdc33/copyOfWorkOutManagement/workouts"

exercise_config = {
    "query":exercise_name,
    "gender":"male",
    "weight_kg":73.5,
    "height_cm":168.78,
    "age":22
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=("workout", "abcd1234+def"))
print(sheet_response.text)