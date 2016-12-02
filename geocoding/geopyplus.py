import json
import os
from geopy.geocoders import GoogleV3, Bing, MapQuest
from geopy.exc import GeocoderQuotaExceeded


class GeoPyPlus:
    def __init__(self, config_path='geopyplus.cfg'):
        config = None
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        self.providers = []
        self.current_index = -1

        # The APIs will be used in the order that they are in the configuration file
        for provider, attributes in config['providers'].iteritems():
            if provider == 'google':
                self.providers.append(GoogleV3(api_key=attributes['api_key']))
            elif provider == 'bing':
                self.providers.append(Bing(api_key=attributes['api_key']))
            elif provider == 'mapquest':
                self.providers.append(MapQuest(api_key=attributes['api_key']))
            else:
                continue

            self.current_index += 1

        self.current_index = 0

    def _increment(self):
        self.current_index += 1
        if self.current_index >= len(self.providers):
            self.current_index = 0

    def geocode(self, query, exactly_one=True, timeout=None):
        starting_index = self.current_index

        while True:
            try:
                return self.providers[self.current_index].geocode(query, exactly_one, timeout)
            except GeocoderQuotaExceeded:
                self._increment()
                if self.current_index == starting_index:
                    raise
