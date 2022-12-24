import requests
from datetime import datetime

USERNAME = "albertwillbedeveloper"
TOKEN = "3ud88xcj9das0ds9au"
pixela_endpoint = "https://pixe.la/v1/users"

# Create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# Encrypt our api
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Upload a pixel in the graph

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?: ")
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# Update a pixel

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20221223"

pixel_corrected_data = {
    "quantity": "30"
}

# pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_corrected_data, headers=headers)
# print(pixel_update_response.text)

# Delete a pixel

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20221223"

# pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)
