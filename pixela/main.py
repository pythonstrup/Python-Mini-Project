import requests
from datetime import datetime, timedelta

# https://pixe.la/@park


USERNAME = "park"
TOKEN = "vkdltjsroqkfwk123"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now() - timedelta(1)
# today = datetime(year=2021, month=8, day=1)

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much time do you spend on your studies?: "),
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210801"

update_params = {
    "quantity": "4.0"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210801"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)