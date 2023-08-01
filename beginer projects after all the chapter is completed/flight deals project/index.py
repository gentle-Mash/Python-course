import requests

# for i in range(7):
#     flight_cost = [1324,956,1618,1072,1175,1964,5074]
#     sheet_put_endpoints = f"https://api.sheety.co/d56279c796fcaee125aa3791536fdc33/copyOfFlightDeals/prices/{i+2}"

#     sheet_inputs  = {
#         "price" : {
#             "lowestPrice" : flight_cost[i]
#         }
#     }
#     sheet_response = requests.put(url=sheet_put_endpoints, json= sheet_inputs)
#     print(sheet_response.text)

# air_trip_endpoint = "https://api.flightapi.io/oneway"


# air_trip_inputs = {
#     "api_key" : "64c4e5a8fcc2fbebfeee33ab",
#     "departure_airport_code" : "DAC",
#     "arrival_airport_code" : "TYO",
#     "departure_date" : "2023-08-01",
#     "number_of_adults" : "1",
#     "number_of_childrens":"0",
#     "number_of_infants" : "0",
#     "cabin_class" : "Business",
#     "currency" : "USD"

# }

# air_trip_response = requests.get(url=air_trip_endpoint, params=air_trip_inputs)
# print(air_trip_response.status_code)