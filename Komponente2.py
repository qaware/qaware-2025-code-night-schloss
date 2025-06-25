import requests

BASE_URL: str = "http://127.0.0.1:8000/"

def get_autoteil(seriennummer: int):
    response = requests.get(BASE_URL + "autoteile/" + str(seriennummer))
    return response.content


if __name__ == '__main__':
    print(get_autoteil(1))
    # TODO: Ergänze die Funktionalität, sodass Kunden & Kolleg*innen mit dem System arbeiten können
