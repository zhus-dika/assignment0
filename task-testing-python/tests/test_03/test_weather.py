import json
from unittest.mock import patch

from weather_03.weather_wrapper import *
from unittest import mock
import unittest


def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)

class TestWeatherWrapper(unittest.TestCase):
    @patch('weather_03.weather_wrapper.requests')
    def test_get(self, requests_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = read_json('tests/test_03/data/response_base_url_ottawa.json')
        requests_mock.get.return_value = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual(1.07, weather_wrapper.get_response_city('Ottawa', BASE_URL)['main']['temp'])

    @patch('weather_03.weather_wrapper.requests')
    def test_error_from_server(self, requests_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 404
        requests_mock.get.return_value = response_mock
        with self.assertRaises(AttributeError):
            weather_wrapper = WeatherWrapper(mock.MagicMock())
            weather_wrapper.get_response_city('aaa', BASE_URL)

    @patch('weather_03.weather_wrapper.requests')
    def test_get_temperature(self, requests_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = read_json('tests/test_03/data/response_base_url_ottawa.json')
        requests_mock.get.return_value = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual(1.07, weather_wrapper.get_temperature('Ottawa'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_temperature(self, requests_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = read_json('tests/test_03/data/response_forecast_url_ottawa.json')
        requests_mock.get.return_value = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual(-0.75, weather_wrapper.get_tomorrow_temperature('Ottawa'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_diff_string_colder(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_base_url_delhi.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_ottawa.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('Weather in Delhi is warmer than in Ottawa by 21 degrees', weather_wrapper.get_diff_string('Delhi', 'Ottawa'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_diff_string_warmer(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_base_url_ottawa.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_delhi.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('Weather in Delhi is colder than in Ottawa by 21 degrees', weather_wrapper.get_diff_string('Delhi', 'Ottawa'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_diff_much_warmer(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_forecast_url_astana.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_astana.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('The weather in Astana tomorrow will be much warmer than today', weather_wrapper.get_tomorrow_diff('Astana'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_diff_warmer(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_forecast_url_delhi.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_delhi.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('The weather in Delhi tomorrow will be warmer than today', weather_wrapper.get_tomorrow_diff('Delhi'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_diff_colder(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_forecast_url_ottawa.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_ottawa.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('The weather in Ottawa tomorrow will be colder than today', weather_wrapper.get_tomorrow_diff('Ottawa'))

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_diff_much_colder(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_forecast_url_chile.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_chile.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('The weather in Chile tomorrow will be much colder than today', weather_wrapper.get_tomorrow_diff('Chile'))\

    @patch('weather_03.weather_wrapper.requests')
    def test_get_tomorrow_diff_same(self, requests_mock):
        response_mock = [mock.MagicMock(), mock.MagicMock()]
        response_mock[0].status_code = 200
        response_mock[0].json.return_value = read_json('tests/test_03/data/response_forecast_url_moscow.json')
        response_mock[1].status_code = 200
        response_mock[1].json.return_value = read_json('tests/test_03/data/response_base_url_moscow.json')
        requests_mock.get.side_effect = response_mock
        weather_wrapper = WeatherWrapper(mock.MagicMock())
        self.assertEqual('The weather in Moscow tomorrow will be the same than today', weather_wrapper.get_tomorrow_diff('Moscow'))
