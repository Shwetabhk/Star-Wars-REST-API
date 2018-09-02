from django_cron import CronJobBase, Schedule
from StarWars.utils.images_download import googleimagesdownload
import os
import requests
import json


class ImageExtract(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'planets.image'

    def do(self):
        try:
            file = open("Planets/images.json", 'w+')
            images = {}
            for page in range(1, 8):
                url = 'https://swapi.co/api/planets/'
                r = requests.get(url, params={'page': page})
                data = r.text
                result = json.loads(data)["results"]
                page_results = []
                for i in result:
                    response = googleimagesdownload()
                    arguments = {
                        "keywords": i['name']+" planet", "limit": 1, "print_urls": True}
                    _, url = response.download(arguments)
                    page_results.append({"name": i['name'], "url": url})
                images[page] = page_results
            print(json.dumps(images), file=file)
        except Exception as e:
            print(e)
