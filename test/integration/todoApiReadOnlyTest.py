import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
#BASE_URL = "https://m0qwfec693.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - READ ONLY test Get TODO')
        url = BASE_URL + "/todos"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        todos = response.json()
        self.assertTrue(len(todos) > 0, "No hay TODOs para probar lectura individual")
    
        first_id = todos[0]['id']
        url = BASE_URL + "/todos/" + first_id
        response = requests.get(url)
        print(f"GET /todos/{first_id} => {response.status_code}")
        self.assertEqual(response.status_code, 200)

        json_response = response.json()
        print('Response Get Todo: ' + str(json_response))
        self.assertIn('text', json_response)

        print('End - READ ONLY test Get TODO')
    