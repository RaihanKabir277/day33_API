# print("day 33 with API starts here")

import requests 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# print(type(response))


