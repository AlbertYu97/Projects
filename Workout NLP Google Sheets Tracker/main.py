import requests
from datetime import datetime
import os
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BASE_LINK = "https://trackapi.nutritionix.com/"
SHEETY_LINK = "https://api.sheety.co/"
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PROJECTNAME = "workoutTracking"
SHEETY_SHEETNAME = "workouts"
TOKEN = os.environ["TOKEN"]
GENDER = "MALE"
WEIGHT_KG = 100
HEIGHT_CM = 193
AGE = 24

# Get the exercise type and duration with Nutritionix API
exercise = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

workout_data = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

workout_response = requests.post(url=f"{BASE_LINK}/v2/natural/exercise", json=workout_data, headers=header)
result = workout_response.json()

exercise_name = result["exercises"][0]["name"]
exercise_duration = result["exercises"][0]["duration_min"]
exercise_calories = result["exercises"][0]["nf_calories"]

# Update Google Sheets with Sheety API

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")

bearer_headers = {
    "Authorization": TOKEN
}

sheet_inputs = {
    "workout":
        {
            "date": date,
            "time": time_string,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
}

exercise_response = requests.post(url=f"{SHEETY_LINK}/{SHEETY_USERNAME}/{SHEETY_PROJECTNAME}/{SHEETY_SHEETNAME}",
                                  json=sheet_inputs,
                                  headers=bearer_headers)
print(exercise_response.text)
