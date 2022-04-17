from twilio.rest import Client
import requests

OWM_API = "https://api.openweathermap.org/data/2.5/onecall"
# MY_LAT = 37.5683    # Seoul
# MY_LON = 126.9778
MY_LAT = 39.343357    # Tianjin 텐진시 7/29 당시 비 많이옴
MY_LON = 117.361649
api_key = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_API, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_next12 = weather_data["hourly"][:12]

# print(response)
# print(weather_data)
# print(hourly_next12[0]["weather"][0]["id"])

how_weather=[]
take_umbrella = False
for hourly_weather in hourly_next12:
    how_weather.append(hourly_weather["weather"][0]["id"])
    if hourly_weather["weather"][0]["id"] < 700:
        take_umbrella = True


print(how_weather)
if take_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella!",
        from_='YOUR_TWILIO',
        to='TO_PHONE_NUMBER'
    )
    print(message.status)