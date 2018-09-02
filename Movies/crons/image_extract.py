from django_cron import CronJobBase, Schedule
from StarWars.utils.images_download import googleimagesdownload
import os
import requests
import json


class ImageExtract(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'movies.image'


    def do(self):
        try:
            file=open("Movies/images.json",'w+')
            images={}
            url = 'https://swapi.co/api/films/'
            r = requests.get(url)
            data = r.text
            result = json.loads(data)["results"]
            img_list=[]
            for i in result:
                response = googleimagesdownload()
                arguments = {
                    "keywords": "star wars " + i['title'], "limit": 1, "print_urls": True}
                _, url = response.download(arguments)
                img_list.append(url)
            images["list"]=img_list
            print(json.dumps(images), file=file)
        except Exception as e:
            print(e)
