from django.db import models
from .userRecommend import data , title, titlebook, titlewhere,databook,datawhere

class Post(models.Model):
    ratings = data
    title = title
    bookratings=databook
    booktitle=titlebook
    whereratings=datawhere
    wheretitle=titlewhere


class Rating(models.Model):
    ratings = data
    title = title
    bookratings=databook
    booktitle=titlebook
    whereratings=datawhere
    wheretitle=titlewhere

class Recommend(models.Model):
    userId =models.CharField(max_length=200) 
    emotion = models.CharField(max_length=200)
    category = models.CharField(max_length=200)