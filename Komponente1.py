from time import time

import requests

from models import Autoteilbeschreibung

BASE_URL: str = "http://127.0.0.1:8000/"


def create_autoteil(beschreibung: Autoteilbeschreibung):
    response = requests.post(BASE_URL + "autoteile/", beschreibung.json())
    return response.status_code


def update_autoteil(beschreibung: Autoteilbeschreibung):
    response = requests.put(BASE_URL + "autoteile/", beschreibung.json())
    return response.status_code

if __name__ == '__main__':
    autoteil = Autoteilbeschreibung(seriennummer=1, zeitstempel=time().__str__())
    print(create_autoteil(autoteil))