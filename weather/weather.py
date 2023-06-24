# %%
import requests

def get_weather_forecast(city):
    API_key = "8510cb3e5b783616c8263b836df0796b"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    try:
        response = requests.get(url)
        # response.raise_for_status()
        data = response.json()
        if data['cod'] != 200:
            print(f"Could not get weather forecast for {city} , Weather API ERROR - {data['message']}")
            return None
        weather_data = {}
        weather_data['description'] = data['weather'][0]['description']
        weather_data['temp_min'] = data['main']['temp_min']
        weather_data['temp_max'] = data['main']['temp_max']
        weather_data['humidity'] = data['main']['humidity']
        weather_data['wind'] = data['wind']
        weather_data['temp_curr'] = data['main']['temp']
        weather_data['city'] = data['name']
        return weather_data


    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", str(e))
        return None

# %%
res = get_weather_forecast("London")
# %%
import argparse

def main():
    # Read the numbers from command line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
        return

    try:
        city = str(sys.argv[1])
        result = get_weather_forecast(city)
        if result is None:
            return
        print(f"Current temperature in {city} is {result['temp_curr']} Kelvin. Temperature in {city} will range from {result['temp_min']} to {result['temp_max']} Kelvin. Wind speed is {result['wind']['speed']} m/s. Humidity is {result['humidity']}%. Weather Forcast is {result['description']}. ")
        
    except ValueError:
        print("Invalid input. Please provide valid city name.")

if __name__ == "__main__":
    main()