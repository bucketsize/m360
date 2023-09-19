import json
import requests
from asyncio import sleep as asleep

def usage():
    OpenWeatherApi="http://api.openweathermap.org/data/2.5/weather?q=bengaluru&appid=%s"
    OpenWeatherApiKey=Cfg['openweathermap_apikey']
    if not OpenWeatherApiKey:
        print("WARN :: OpenWeatherApiKey not defined!")
        OpenWeatherApiKey = "__UNKNOWN__"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(OpenWeatherApi % OpenWeatherApiKey, headers=headers)
    if response.status_code != 200:
        print("OpenWeatherApi Error:", response.content)
        return 0,0,"?"
    res = json.loads(response.content)
    temperature = float(res["main"]["temp"]) - 273.15
    summary = res["weather"][0]["description"]
    humidity = float(res["main"]["humidity"])
    return temperature, humidity, summary

async def co(MTAB={}):
    while True:
        t,h,s=usage()
        MTAB['weather_temperature']=t
        MTAB['weather_humidity']=h
        MTAB['weather_summary']=s
        await asleep(1)
