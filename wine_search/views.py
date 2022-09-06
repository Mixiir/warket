from django.shortcuts import render
from .forms import WineSearchImageUpload
import decouple
import requests
import json
from django.contrib import messages


def upload_file(request):
    global wine_name
    if request.method == 'POST':
        form = WineSearchImageUpload(request.POST)
        if form.is_valid():
            url = "https://wine-recognition2.p.rapidapi.com/v1/results"
            querystring = {"n": "1"}
            payload = f"url={request.POST['url']}"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Key": decouple.config('RAPIDAPI_KEY'),
                "X-RapidAPI-Host": "wine-recognition2.p.rapidapi.com"
            }
            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            data = response.json()

            # TODO results = data.get('results')
            # if results:
            # utility function checks whether the results are empty or not and if keys value is an list?

            status = data['results'][0]['status']['message']
            image = data['results'][0]['name']
            info = data['results'][0]['entities'][0]['classes']
            name = list(info.keys())[0]
            year = int(name[-4:])
            messages.success(request, f'Wine image has been identified')
            return render(request, 'search.html', {'form': form,
                                                   'response': response.text,
                                                   'image': image,
                                                   'status': status,
                                                   'info': info,
                                                   'year': year})
        # TODO make all_auction_listings returns into one return. Context needs to be changed to fit for it.
        else:
            form = WineSearchImageUpload()
        return render(request, 'search.html', {'form': form})
    else:
        form = WineSearchImageUpload()
        return render(request, 'search.html', {'form': form})
