# Weather Project

A small Python program that fetches the current weather from the
Open-Meteo API and saves it to a JSON file.

## What it does
- Sends a GET request to the Open-Meteo API using the requests library
- Reads the temperature and wind speed from the JSON response
- Saves the result to weather.json
- Handles errors (timeout, no internet connection, server error)

## How to run
1. Install the library: pip install requests
2. Run: python my_code.py

## Notes
- The location is set by latitude and longitude inside the code.
- No API key is needed.