from django.shortcuts import render
from .forms import WineSearchImageUpload
import decouple
import requests
import json


def upload_file(request):
    if request.method == 'POST':
        form = WineSearchImageUpload(request.POST)
        if form.is_valid():
            url = "https://wine-recognition2.p.rapidapi.com/v1/results"
            querystring = {"n": "3"}
            payload = f"url={request.POST['url']}"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Key": decouple.config('RAPIDAPI_KEY'),
                "X-RapidAPI-Host": "wine-recognition2.p.rapidapi.com"
            }
            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            data = response.json()
            status = data['results'][0]['status']['message']
            image = data['results'][0]['name']
            info = data['results'][0]['entities'][0]['classes']
            return render(request, 'search.html', {'form': form,
                                                   'response': response.text,
                                                   'image': image,
                                                   'status': status,
                                                   'info': info})
        else:
            form = WineSearchImageUpload()
        return render(request, 'search.html', {'form': form})
    else:
        form = WineSearchImageUpload()
        return render(request, 'search.html', {'form': form})
