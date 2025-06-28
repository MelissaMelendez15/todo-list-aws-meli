import os
import unittest
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApiReadOnly(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - READ ONLY test List TODO')
        url = BASE_URL + "/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(response.status_code, 200, f"Error en la petición API a {url}")
        self.assertTrue(response.json())
        print('End - READ ONLY test List TODO')

    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - READ ONLY test Get TODO')
        url = BASE_URL + "/todos/1"
        response = requests.get(url)
        print('Response Get Todo: ' + str(response.json()))
        self.assertEqual(response.status_code, 200, f"Error en la petición API a {url}")
        print('End - READ ONLY test Get TODO')