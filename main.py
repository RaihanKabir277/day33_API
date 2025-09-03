# print("day 33 with API starts here")

import requests 

MY_LAT = 51.507351
MY_LON = -0.127758


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(type(response))

# for get the response code 
# print(response.status_code)

# if response.status_code == 404:
#     raise Exception("That resource does not exist")
# elif response.status_code == 401:
#     raise Exception("you are not authorised to access this data")

#------------ there is a error handing in request documentation -------
# response.raise_for_status()

# ----- json data fetch ----
# data = response.json()
# print(data)

# ------ want to specific short of data -----
# data = response.json()["iss_position"]
# print(data)
# data = response.json()["iss_position"]["longitude"]
# print(data)

# -------paricularly fetch longtitude and latitude -------
# data = response.json()

# longtitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longtitude, latitude)
# print(iss_position)

# -------- sunset and sunrise times API -------

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LON,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

