import decouple
import requests


def search_api(address):
    url = "https://wine-recognition2.p.rapidapi.com/v1/results"
    querystring = {"n": "5"}
    payload = f"url={address}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": decouple.config('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "wine-recognition2.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    return response.text
