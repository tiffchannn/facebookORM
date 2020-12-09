from django.shortcuts import render, HttpResponse
from .models import User, Post, Comment

# Create your views here.
def index(request):
    return HttpResponse("Hello ORM")