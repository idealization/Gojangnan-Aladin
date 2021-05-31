from django.db import models
# Create your models here.


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    ISBN = models.TextField()
    price = models.TextField()

    published_year = models.TextField()
    original_title = models.TextField()
    language = models.TextField()
    rating = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.title  # subject를 반환하는 함수
