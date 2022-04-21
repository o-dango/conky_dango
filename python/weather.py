#!/usr/bin/python
from datetime import datetime, timezone
import pyowm
import requests
from api_keys import open_weather_key

# globals
TABS = "\t\t\t\t"
HOME = "/home/camilla"

# classes
class Data():
    def __init__(self):
        # set your own OWM token and home city
        self.token = open_weather_key
        self.location = "Lappeenranta,FI"


# functions
def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def convertTime(date_time_str):
    date_time_str = date_time_str.split("+")
    return utc_to_local(datetime.strptime(date_time_str[0], '%Y-%m-%d %H:%M:%S'))


def saveIcon(image_url):
    img_data = requests.get(image_url).content
    try:
        with open(HOME + '/.config/conky/dango_conky/assets/weather_icon.png', 'wb') as handler:
            handler.write(img_data)
    except:
        print(":(")

def printWeather(w, city):
    wind = w.get_wind()
    temp = w.get_temperature(unit='celsius')
    sunrise = convertTime(w.get_sunrise_time('iso'))
    sunset = convertTime(w.get_sunset_time('iso'))
    image_url = w.get_weather_icon_url()
    saveIcon(image_url)

    print(TABS + "Location: " + city + "\n"
        + TABS + "Wind: " + str(wind['speed']) + "m/s" + "\n"
        + TABS + "Temperature: " + str(round(temp['temp'])) + "°C" + "\n"
        + TABS + "Sunrise: " + sunrise.strftime("%H:%M:%S, %m/%d/%Y") + "\n"
        + TABS + "Sunset: " + sunset.strftime("%H:%M:%S, %m/%d/%Y"))


def printForecast(w, date):
    temp = w.get_temperature(unit='celsius')
    status = w.get_detailed_status()

    print("\n" + TABS + date + "\n"
        + TABS + "Temperature" + str(round(temp['temp'])) + "°C" + "\n"
        + TABS + "Weather: " + status)


def getWeather(data):
    owm = pyowm.OWM(data.token)
    observation = owm.weather_at_place(data.location)
    city = observation.get_location().get_name()
    weather = observation.get_weather()
    printWeather(weather, city)


def getForecast(data):
    owm = pyowm.OWM(data.token)
    current_date = datetime.now().strftime("%Y-%m-%d")
    fc = owm.three_hours_forecast(data.location)
    f = fc.get_forecast()
    city = f.get_location().get_name()
    w = []
    for weather in f:
        weather_date = convertTime(weather.get_reference_time('iso'))
        date = weather_date.strftime("%Y-%m-%d")
        if date != current_date:
            d = date + " 12:00:00+00"
            try:
                w.append(fc.get_weather_at(d))
            except:
                break

    w = list(set(w))
    for forecast in w:
        forecast_date = convertTime(forecast.get_reference_time('iso')).strftime("%Y-%m-%d")
        printForecast(forecast, forecast_date)


def main():
    data = Data()
    getWeather(data)
    getForecast(data)


if __name__ == '__main__':
    main()
