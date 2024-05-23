import requests
from rich import print
from datetime import datetime

# ------------------------------------------------------------------

def get_api_response(api_url):
  """Makes a call to an API and returns the API response in json format"""
  api_response = requests.get(api_url)
  api_response_in_json_format = api_response.json()
  return api_response_in_json_format

# ------------------------------------------------------------------
  
def display_current_weather(city):
  """Displays the current weather conditions for a city"""
  
  api_key = "cf14b4c0f0c0d7a973ee3b4e430t2bo5"
  api_url_current_weather = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=imperial"
  current_weather = get_api_response(api_url_current_weather)
  current_temperature = current_weather['temperature']['current']
  
  display_temperature(f"Today in {city}", current_temperature)

# ----------------------------------------------------------------

def timestamp_to_day_of_week(timestamp):
  """Converts a timestamp to the full length day of the week"""
  date = datetime.fromtimestamp(timestamp)
  day_of_week = date.strftime("%A")
  return day_of_week

# ----------------------------------------------------------------
def display_temperature(day_of_week, temperature, units='F'):
  """Displays the formatted temperature message - day and temperature"""
  print(f"[medium_violet_red]{day_of_week}[/medium_violet_red]: {round(temperature)}°{units}")

# ----------------------------------------------------------------

def display_weather_forecast(city):
  """Displays the forecasted weather conditions for a city"""
  api_key = "cf14b4c0f0c0d7a973ee3b4e430t2bo5"
  api_url_weather_forecast = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}&units=imperial"
  
  forecast_weather = get_api_response(api_url_weather_forecast)
  
  print("\n[green bold]Forecast:[/green bold]")
  
  for day in forecast_weather['daily']:
    timestamp = day['time']
    date = datetime.fromtimestamp(timestamp)
    day_of_week = timestamp_to_day_of_week(timestamp)
    temperature = day['temperature']['day']
    # the first day returned for the forecast is today. We want to start with tomorrow's information
    if date.date() != datetime.today().date():
      display_temperature(day_of_week, temperature)

# ----------------------------------------------------------------
def welcome():
  """Displays a welcome message"""
  print("🌞 [purple bold]Welcome to Weather Watch 🌞\n[/purple bold]") 

# ----------------------------------------------------------------
welcome()   
city = input ("Enter a city name: ")
city = city.strip().title()

if city:
  display_current_weather(city)
  display_weather_forecast(city)
else:
  print("Please enter a city")