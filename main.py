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

import time
import datetime
import os
import requests

from functions import (
     save_query_file,
     weather,
     rain_or_not,
)


def check_weather():
    with open("", "r") as f:#


# if file does exist
def main():
    file = os.path.exists("")
    # latitude, longitude


# ask the user for the date
today = datetime.date.today()
user_date_weather = input("Enter a date in YYYY-mm-dd format or press enter to see the next day: ")
if

# if no date inserted then it will automatically go to the next day.
if not user_date_weather:
    next_day = datetime.date.today() + time.
    # + 1? how