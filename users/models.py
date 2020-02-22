from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='DPs')
    api_key=models.CharField(max_length=500,null=True)
    device_name=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.user.username+"---->"+self.user.first_name+" "+self.user.last_name
    

    def save(self):
        api_key=self.api_key
        device_name=self.device_name
        super().save()
        img=Image.open(self.image.path)
        if img.height>200 or img.width>200:
            op=(200,200)
            img.thumbnail(op)
            img.save(self.image.path)

class Feedback(models.Model):
    pak=92
    india=91
    canada=1
    china=86
    france=33
    australia=61
    choices=(
        (india,'India'),
        (pak,'Pakistan'),
        (china,'China'),
        (canada,'Canada'),
        (france,'France'),
        (australia,'Australia'),

    )
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    country=models.IntegerField(choices=choices)
    number=models.CharField(max_length=15)
    feedback=models.TextField(max_length=1000)

    def __str__(self):
        return self.name + "  "+ self.surname
    




