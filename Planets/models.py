from django.db import models
import random
import os


def get_file_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename=str(random.randint(0,1000000))
    name,ext=get_file_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "planets/planet{final_filename}".format(final_filename=final_filename)



class Planet(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True)