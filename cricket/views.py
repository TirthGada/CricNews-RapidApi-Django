import requests
from django.http import JsonResponse
from django.shortcuts import render

def cricket_data(request):
    api_key = 'YOUR_RAPIDAPI_KEY'
    url = 'https://cricket-live-data.p.rapidapi.com/results'

    headers = {
        'X-RapidAPI-Key': '2938a1918fmshca60bc293795253p18f0fajsnd20cda63e045',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    results=data['results']

    context ={
        'results':results
    }

    return render(request, 'cricket/cricketdata.html', context)
