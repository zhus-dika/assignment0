from simple_library_01.functions import is_leap
from tree_utils_02.tree import Tree
from unittest import mock
from unittest.mock import MagicMock
from tree_utils_02.size_tree import *
from weather_03.weather_wrapper import *
import tempfile
import os
from tree_utils_02.node import FileNode
requests = mock.Mock()

if __name__ == '__main__':
    #print(is_leap(2021))

    #print(Tree().get('./', dirs_only=False))
    token = '34802d0758d006f06128a6a946df50bd'

    wrapper = WeatherWrapper(token)
    print(wrapper.get_response_city('Chile', FORECAST_URL))
