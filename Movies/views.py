from django.http import JsonResponse
from Movies.utils.movies_images import IMAGES
import requests
import json


def movies(request):
    url = 'https://swapi.co/api/films/'
    r = requests.get(url)
    data = r.text
    result = json.loads(data)["results"]
    return JsonResponse({"data": result, "images": IMAGES})
