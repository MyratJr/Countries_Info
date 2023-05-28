from django.db import models
from django.utils import timezone


class Places(models.Model):
    capital = models.CharField(max_length=100)
    country=models.CharField(max_length=30)
    flag=models.CharField(max_length=9999)
    desc = models.TextField()
    continent=models.CharField(max_length=100)
    president=models.CharField(max_length=100)
    square=models.CharField(max_length=100)
    population=models.CharField(max_length=100)
    currency=models.CharField(max_length=100)
    interests = models.BooleanField(default=False)
    top_place = models.BooleanField(default=False)
    
    def __str__(self):
        if self.country:
            return self.country
        else:
            return self.desc
    class Meta:
        ordering = ['country']

class PropertyImage(models.Model):
    property = models.ForeignKey(Places, default=None ,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=9999)
    
    def __str__(self):
        return str(self.property)

class HomeSlide(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
class SlideImage(models.Model):
    property = models.ForeignKey(HomeSlide, default=None ,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=9999)

    def __str__(self):
        return str(self.property)

class signup(models.Model):
    Username=models.CharField(max_length=30)
    Phone=models.CharField(max_length=20)
    Email=models.EmailField()


    def __str__(self):
        return self.Username

class News(models.Model):
    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def shorten(self):
        return self.desc[:125]


