import pandas as pd
import json
import requests


class Geocodio():
    """Class to retrieve geocodes from Geocodio"""
    def __init__(self):
        self.url = 'url'
        self.key = 'your_api_key'
        self.addresses = None

    def get_geocodes(self):
        """Get Geocodes"""

        endpoint = 'geocode'
        url = f"{self.url}{endpoint}"


        params = {
            'api_key': self.key,
            'fields': ''      # Add the fields you want 
            'limit': 1
            }

        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url=url, json=self.addresses, headers=headers, params=params)

        if response.status_code == 200:
            geocodes = response.json()
            return geocodes

        else:
            geocodes = None
            print('Error', response.status_code, response.text)
            
            return None
