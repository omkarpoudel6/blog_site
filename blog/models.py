from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()
class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.FileField(upload_to="user_images")



    def __str__(self):
        return self.user.username


class Category(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    title=models.CharField(max_length=100)
    overview=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    comment_count=models.IntegerField(default=0)
    views_count=models.IntegerField(default=0)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail=models.FileField(upload_to="thumbnails")
    categories=models.ManyToManyField(Category)
    featured=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Signup(models.Model):
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email