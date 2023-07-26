import requests
from datetime import datetime

endpoint = "https://pixe.la/v1/users"
USERNAME = "jannat"
TOKEN = "skdjhIUI687auigt*&^%KJHG^*$LAkd8582-#JIK%PU"

user = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=endpoint, json=user)
# print(response.text)

graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN" : TOKEN,
}

graph_config = {
    "id" : "graph1",
    "name" : "Coding graph",
    "unit" : "hour",
    "type" : "int",
    "color" : "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

graph_value_endpoint = f"{graph_endpoint}/graph1"
# yesterday = datetime(year=2023, month=7, day=25)
today = datetime.now()
today_date = today.strftime("%Y%m%d")

graph_values = {
    "date" : today_date,
    "quantity" : input("How many hours did you code today? ")
}

response = requests.post(url=graph_value_endpoint, json=graph_values, headers=header)
print(response.text)






graph_update_endpoint = f"{graph_value_endpoint}/{today_date}"
# print(graph_update_endpoint)
graph_update = {
    "quantity" : "5",
}

# response = requests.put(url=graph_update_endpoint, json=graph_update, headers=header)
# print(response.text)


graph_delete_endpoint = graph_update_endpoint

# response = requests.delete(url=graph_delete_endpoint, headers=header)
# print(response.text)