import requests
from datetime import datetime
from pixela_username_token import *

pixela_endpoint = "https://pixe.la/v1/users"
header = {
    "X-USER-TOKEN": TOKEN
}
date = datetime.today()
formatted_date = date.strftime("%Y%m%d")

post_params = {
    "date": formatted_date,
    "quantity": input("How many hours did you code?- ")
}
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=post_endpoint, json=post_params, headers=header)
a = response.json()
if a["isSuccess"]:
    print("Habit tracker Updated!")
    print(f"To view- {GRAPH}")
else:
    print("Unsuccessful to update\nPlease try again.")

