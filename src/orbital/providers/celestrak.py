"""
Interface for the Celestrak API.

Classes:   
    Celestrak
"""

import requests
import time
from ..parsers import from_celestrak

class Celestrak:
    """
    Object allowing for retrieval of orbital elements from Celestrak.

    Methods:
    retrieve_omm(norad_id: string)
        returns OMM data model object after polling the Celestrak REST API
    """
    BASE_URL = "https://celestrak.org/NORAD/elements/gp.php"

    def __init__(self):
        self._session = requests.Session()

    def retrieve_omm(self, norad_id):
        """
        Fetches the OMM GP data for a particular object from the Celestrak API

        Args:
            norad_id: int -> unique sequential identifier used to designate tracked objects in orbit

        Return:
            OMM data model object

        Exceptions:
            RuntimeError -> Unexpected exits
            requests.Timeout
        """

        omm_json = self._get(params ={
            "FORMAT": "JSON",
            "CATNR": norad_id
        })

        data = omm_json[0]

        return from_celestrak(data)

    def _get(self, params):
        """HTTP Get request to Celestrak base URL"""
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