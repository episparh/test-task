import unittest

from open_weather_api import get_response

appid = "08f86f73fb82f39bab545fc122868405"
cities = {"BG": "Sofia",
          "AT": "Vienna",
          "BE": "Brussels",
          "FR": "Paris",
          "DE": "Berlin",
          "IT": "Rome",
          "ES": "Madrid",
          "PL": "Warsaw",
          "PT": "Lisbon",
          "GR": "Athens"}


class TestStringMethods(unittest.TestCase):

    def test_api_get(self):
        country_codes_failures = {}
        temp_out_of_range = {}
        for key in cities:
            json = get_response(cities[key], appid)
            temp = json.get("main").get("temp") - 273.15
            country = json.get("sys").get("country")
            if (temp < -25) or (temp > 40):
                temp_out_of_range[cities[key]] = temp
            if country != key:
                country_codes_failures[key] = country
        self.assertEqual(temp_out_of_range, {})
        self.assertEqual(country_codes_failures, {})


if __name__ == '__main__':
    unittest.main()
