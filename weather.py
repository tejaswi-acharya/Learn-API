import requests

city= input("Enter the name of the city:")
api_key="9f8b40a90f6d41c60c8fa7f9d04e80c9"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
weather=response.json()
# print(weather)

if response.status_code == 200:
    print(f"\nCity: {weather['name']}")
    print(f"Temperature: {weather['main']['temp']} °C")
    print(f"Condition: {weather['weather'][0]['description']}")
else:
    print("Error:", weather.get("message", "City not found or invalid input"))
    

# {'coord': {'lon': 85.3167, 'lat': 27.7167},
#  'weather': [{'id': 803, 'main': 'Clouds',
#    'description': 'broken clouds', 'icon': '04d'}], 
#    'base': 'stations',
#  'main': {'temp': 27.28, 'feels_like': 30.26, 'temp_min': 27.28, 'temp_max': 27.28, 'pressure': 1006, 'humidity': 79, 'sea_level': 1006, 'grnd_level': 846}, 'visibility': 10000, 'wind': {'speed': 1.6, 'deg': 209, 'gust': 2.28}, 'clouds': {'all': 79}, 'dt': 1750938961, 'sys': {'country': 'NP', 'sunrise': 1750893887, 'sunset': 1750943888}, 
# 'timezone': 20700,
#  'id': 1283240, 
#  'name': 'Kathmandu',
#    'cod': 200}
