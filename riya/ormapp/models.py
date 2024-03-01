from django.db import models
from django.contrib import admin
class Book(models.Model):
   book_id=models.IntegerField(primary_key=True);
   book_name=models.CharField(max_length=20);
   price=models.IntegerField();
   author_name=models.CharField(max_length=50);
   author_email=models.EmailField();
class BookAdmin(admin.ModelAdmin):
  list_display=("book_id","book_name","price","author_name","author_email");



