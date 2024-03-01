# Ex02 Django ORM Web Application
## Date: 01/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram


![alt text](<Screenshot 2024-03-01 093007.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py

from django.contrib import admin
from .models import book,bookAdmin
admin.site.register(book,bookAdmin)
```

## OUTPUT

![alt text](<Screenshot 2024-03-01 091026.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
