"""
Interface for the Celestrak API
"""

import requests
import time
from ..parsers import from_celestrak

class Celestrak:
    BASE_URL = "https://celestrak.org/NORAD/elements/gp.php"

    def __init__(self):
        self._session = requests.Session()

    def retrieve_omm(self, norad_id):
        omm_json = self._get(params ={
            "FORMAT": "JSON",
            "CATNR": norad_id
        })

        data = omm_json[0]

        return from_celestrak(data)

    def _get(self, params):
        for attempt in range(3):
            try:
                response = self._session.get(
                    self.BASE_URL,
                    params=params,
                    timeout=(5, 30)
                )

                response.raise_for_status()
                return response.json()
            
            except requests.Timeout:
                if attempt == 2:
                    raise

                time.sleep(attempt ** 2)
        raise RuntimeError("Unexpected loop exit.")