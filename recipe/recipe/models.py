
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    description = models.TextField() 
    instructions = models.TextField()
    reqtime = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"

