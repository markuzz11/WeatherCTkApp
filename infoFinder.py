import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import pyowm

import keys

class PlaceInfo:
    owm = pyowm.OWM(keys.owmkey)
    mgr = owm.weather_manager()
    geolocator = Nominatim(user_agent=keys.mail)

    def __init__(self, place):
        self.place = place

    def getTemp(self):
        observation = self.mgr.weather_at_place(self.place)
        obsWtr = observation.weather
        temp = obsWtr.temperature('celsius')['temp']
        return int(temp)

    def getTime(self):
        city = self.place.split()[0][:-1]

        location = self.geolocator.geocode(city)

        tF = TimezoneFinder()
        cityLatitude = location.latitude
        cityLongitude = location.longitude
        timezoneStr = tF.timezone_at(lng=cityLongitude, lat=cityLatitude)
        timezone = pytz.timezone(timezoneStr)
        time = datetime.now(timezone)

        hours_minutes = time.strftime("%H:%M")
        return hours_minutes