import json
import urllib.error
import urllib.request

url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}"


def get_response(city, appid):
    return json.load(urllib.request.urlopen(url.format(city=city, appid=appid)))
