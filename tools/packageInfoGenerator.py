import random
import time

import requests

BASE_URL: str = "http://127.0.0.1:8000/"

BRANDS = ["BMV", "NORD", "WV"]

def send(data: dict):
    response = requests.post(BASE_URL + "autoteile/", str(data).replace("\'", "\""))
    return response.status_code, response.content


def get_random_element(data: list) -> str:
    return data[random.randint(0, len(data) - 1)]


def generate_info() -> dict:
    # TODO: Füge relevante Daten hinzu
    pass


if __name__ == '__main__':
    while True:
        part_info = generate_info()
        response = send(part_info)
        print(f"Sent package info: {part_info}")
        time.sleep(2)

