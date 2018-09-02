from django.shortcuts import render, redirect
from django.http import JsonResponse
from Planets.utils.planet_images import IMAGES
from Planets.forms import PlanetForm
from Planets.models import Planet
from Planets.serializers import PlanetSerializer
import requests
import json


def planets_template(request):
    if request.method == "GET":
        return render(request, "planets.html", {})


def add_planets(request):
    if request.method == "POST":
        form = PlanetForm(request.POST, request.FILES)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/add_planets')
    else:
        form = PlanetForm()
        return render(request, "add_planets.html", {"form": form})


def get_user_planets(request):
    planets = Planet.objects.all()
    result = PlanetSerializer(planets, many=True)
    return JsonResponse(result.data, safe=False)


def planets(request):
    if request.method == "GET":
        try:
            page = int(request.GET["page"])
        except:
            page = 1
        url = 'https://swapi.co/api/planets/'
        r = requests.get(url, params={'page': page})
        data = r.text
        result = json.loads(data)["results"]
        return JsonResponse({"data": result, "images": IMAGES[str(page)]})


def search_planets(request):
    if request.method == "GET":
        try:
            search = request.GET["search"]
            url = 'https://swapi.co/api/planets/'
            r = requests.get(url, params={'search': search})
            data = r.text
            result = json.loads(data)["results"]
            images = []
            for i in IMAGES:
                images.extend(IMAGES[i])
            return JsonResponse({"data": result, "images": images})
        except:
            return JsonResponse({})
