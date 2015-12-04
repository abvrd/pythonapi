from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from datetime import datetime
import feedparser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from pprint import pprint

# Create your views here.
def home(request):
    return render(request, 'api/home.html', {'date': datetime.now()})

def feed(request):
    link = 'http://movieweb.com/rss/movie-news/'
    d = feedparser.parse(link)
    title = d.feed.title
    desc = d.feed.description

    return render(request, 'api/feed.html', {'title': title, 'desc': desc, 'items': d.entries})

@api_view(['GET', 'POST'])
def movies(request):
    """
    List all movies news
    """
    if request.method == 'GET':
        link = 'http://movieweb.com/rss/movie-news/'
        d = feedparser.parse(link)
        for entry in d.entries:
            #remove python date objet for output
            entry.pop("published_parsed", None)

        output = [d.feed.title, d.feed.description, d.entries]
        return Response(output)
    elif request.method == 'POST':

        return Response("created", status=status.HTTP_201_CREATED)


