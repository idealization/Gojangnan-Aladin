from django.contrib import admin

# Register your models here.
from .models import Book
# 해당 폴더의 models.py 의 파일에서 Question 이란 class 를 import


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'ISBN', 'author', 'original title']


admin.site.register(Book, BookAdmin)
