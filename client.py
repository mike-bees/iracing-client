import logging
from enum import IntEnum

import requests
from requests import Response

BASE_URL = "https://members-ng.iracing.com"


class EventType(IntEnum):
    PRACTICE = 2
    QUALIFY = 3
    TIME_TRIAL = 4
    RACE = 5


class IRacingApiClient():
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.connected = False

    def _get_linked_document(self, response: Response) -> dict:
        response_body = response.json()
        link_url = response_body["link"]
        response = requests.get(url=link_url)
        if response.status_code != 200:
            logging.error(
                "Error getting linked document. Response %s", response)
            return
        return response.json()

    def connect(self):
        url = f"{BASE_URL}/auth"
        data = {
            "email": self.email,
            "password": self.password
        }
        response = requests.post(url=url, data=data)
        if response.status_code != 200:
            logging.error("Error connecting. Response %s", response)
            return
        logging.info("Connected.")
        self.connected = True
        self.cookies = response.cookies

    def get_documentation(self) -> dict:
        if not self.connected:
            logging.error("Not connected.")
            return
        url = f"{BASE_URL}/data/doc"
        response = requests.get(url=url, cookies=self.cookies)
        if response.status_code != 200:
            logging.error("Error getting documentation. Response %s", response)
            return
        return response.json()

    def get_series_seasons(self, include_series: bool) -> dict:
        if not self.connected:
            logging.error("Not connected.")
            return
        url = f"{BASE_URL}/data/series/seasons"
        params = {
            "include_series": include_series
        }
        response = requests.get(url=url, cookies=self.cookies, params=params)
        if response.status_code != 200:
            logging.error(
                "Error getting series seasons. Response %s", response)
            return
        return self._get_linked_document(response)

    def get_season_results(self, season_id: int, event_type: EventType = None, race_week_num: int = None) -> dict:
        if not self.connected:
            logging.error("Not connected.")
            return
        url = f"{BASE_URL}/data/results/season_results"
        params = {
            "season_id": season_id
        }
        if event_type:
            params["event_type"] = event_type
        if race_week_num:
            params["race_week_num"] = race_week_num
        response = requests.get(url=url, cookies=self.cookies, params=params)
        if response.status_code != 200:
            logging.error(
                "Error getting season results. Response %s", response)
            return
        return self._get_linked_document(response)
