# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://pogoda.vtomske.ru/'  # Сам сайт прогноза погоды
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}  # User-Agent
# full_page = requests.get(url, headers=headers)  # Получаем HTML разметку сайта
# soup = BeautifulSoup(full_page.content, 'html.parser')  # Варим суп из 7 разметок
#
#
# wd = soup.find("div", class_="left")  # 1 способ
# wd_details = soup.find("div", class_="details")
# print(wd.text)
# print(wd_details.text)


import requests
import json
city_name = input("Enter city:")
API_key = '6af77e2869f7fe9c97d32d743ded2eea'
api_geocoding = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
response = requests.get(api_geocoding)
json_data = json.loads(response.text)


for data in json_data:
    lat = data['lat']
    lon = data['lon']


api_url_base = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
response = requests.get(api_url_base, params={'units': 'metric', 'lang': 'ru'})
json_data = json.loads(response.text)
print(json_data)
print("conditions:", json_data['weather'][0]['description'])
print("temp:", json_data['main']['temp'])
print("temp_min:", json_data['main']['temp_min'])
print("temp_max:", json_data['main']['temp_max'])
print("pressure:", json_data['main']['pressure'])
print("humidity:", json_data['main']['humidity'])
print("visibility:", json_data['visibility'])
print("wind speed:", json_data['wind']['speed'])
