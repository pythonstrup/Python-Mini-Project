import requests
from datetime import datetime

MY_LAT = 37.566536
MY_LONG = 126.977966

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code == 404:
#     raise Exception("That resource does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
# response.raise_for_status()
#
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)







