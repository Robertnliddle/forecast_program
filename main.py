# Rain forecast program
"""
1. ask the user for a date in "YYYY-mm-dd" format to check the weather.
2. if no date, then it will be the next day
3. Request an api to fetch the weather status given to the date
4. The possible precipitation states are:
  - "It will rain" for a result greater than 0.0. Print the precipitation value for the user for example
  - "It will not rain" for a result equal to 0.0
  - "I don't know" when there is no result or the result is negative
5. Save the query results to a file

hints:
- Use Python's `datetime` module to manipulate dates.
- Use the `requests` library to make API requests.
- Use Google Maps or OpenStreetMap to get the latitude and longitude values for the city you want to check
- Remember to handle exceptions that may occur during the API request.
- Use Python's file handling methods to read and write to a file.
- Validate the user input to ensure it's in the correct format.

"""

api_documentation = "https://open-meteo.com/en/docs"

import datetime
import os
import requests
import geocoder


def check_weather():
    with open("", "r") as f:


def save_query_file(query_results):
    with open(query_results, "w") as f:

def weather(latitude, longitude, provided_date):
    api_endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily="
    f"precipitation_sum&timezone=Europe%2FLondon&start_date={provided_date}&end_date={provided_date}"

    response = request.get()

    # rain rapport / if it will rain or not / don't know
def rain_or_not(weather_report):
    if weather_report > 0.0:
        print(f"It will rain {weather_report} mm")
    elif weather_report == 0.0:
        print("It will not rain")
    else:
        print("I don't know")


# if file does exist
def main():
    file = os.path.exists("")

# ask the user for the date
today = datetime.date.today()
user_date_weather = input("Enter a date in YYYY-mm-dd format or press enter to see the next day: ")

if not user_date_weather:
    next_day = datetime.date.today() + datetime.timedelta(days=1)

#get users location
latitude = input("Enter longitude: ")
longitude = input("Enter longitude: ")


