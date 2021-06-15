from django.db import models
from .userRecommend import data , title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Rating(models.Model):
    ratings = data
    title = title