from django.db import models
from django.urls import reverse 
# Create your models here.

class bookSnapShot(models.Model):
    name = models.CharField(max_length=50,default='NAN')
    author = models.CharField(max_length=30,default='NAN')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detailbook',args=[str(self.id)])
    
class LOG_DB(models.Model):
    user_id = models.CharField(max_length=100)
    book_id = models.CharField(max_length=100)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + ',' + str(self.timestamp)