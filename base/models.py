from codecs import backslashreplace_errors
from distutils.command.upload import upload
from os import truncate
from pydoc import describe
from tkinter import CASCADE
from typing import Text
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    title = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.TextField(max_length=200)
    cost = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=truncate)
    description = models.TextField(max_length=400, blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='static/images')

    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self) -> str:
        return str(self.owner)

class Profile(models.Model):
    MALE = "Male"
    FEMALE = "Female"
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(
        choices=GENDERS,
        max_length=10,
        null=True
    )

    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    surname = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(blank=True, null=True)
    balance = models.IntegerField(default=0)
    status = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(blank=True)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.product)