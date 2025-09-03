
import requests 
from datetime import datetime


MY_LAT = 23.810331
MY_LON = 90.412521


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
    "formatted" : 0,     #change the time format
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  #as here two list after split("T") so [1] means the second list now split(":") and last [0] means that now it will take the 1st value of seperated second list.
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)   

time_now = datetime.now()
print(time_now.hour)