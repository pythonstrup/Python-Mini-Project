
# response = requests.get(sheety_endpoint)
# result = response.json()
# pprint(result)
#
# i = 2
# for city in result["prices"]:
#     sheety_put = {
#         "price": {
#             # "city": city["city"],
#             "iataCode": "TESTING",
#             # "id": city["id"],
#             # "lowestPrice": city["lowestPrice"]
#         }
#     }
#
#     sheet_response = requests.put(f"{sheety_endpoint}/{i}", json=sheety_put)
#     print(sheet_response.text)
#     i += 1
#
# response = requests.get(sheety_endpoint)
# pprint(response.json())