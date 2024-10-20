from django.db import models
import vobject
from django.utils import timezone


# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)

    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class Schedule(models.Model):
    friend_name = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    dtstart = models.DateTimeField()
    dtend = models.DateTimeField()
    location = models.CharField(max_length=50)
    ical = models.FileField(blank=True, null=True)
    dtend = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.friend_name
    

    

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    