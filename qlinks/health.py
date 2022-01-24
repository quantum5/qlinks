import requests


def check_url(url):
    return 200 <= requests.get(url).status_code < 400
