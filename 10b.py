import json
# Load the JSON data from file
with open('10bweather_data.json') as f:
    data = json.load(f)
# Extract the required weather data
curr_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_desc = data['weather'][0]['description']
# Display the weather data
print(f"Current temperature: {curr_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")