from django.db import models

# Create your models here.

# Create a facebook wall - Only the wall feature with posts and comments
# (except likes, as this will be covered in the many-to-many section)

# What Models would you need?
# Classes:
# - users
  # name
  # email
  # age
  # location

# wall?
  # - comments
  # - pictures
  # - posts
  # - date


# What tables would you need in your database?


# What relationships would they have to each other?
# ever user has a wall

class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  age = models.IntegerField()
  location = models.CharField(max_length=255)

class Post(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  posts = models.TextField()
  date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
  post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)

