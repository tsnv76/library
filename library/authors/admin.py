from django.contrib import admin
from .models import Author, Bio, Book

admin.site.register(Author)
admin.site.register(Bio)
admin.site.register(Book)
