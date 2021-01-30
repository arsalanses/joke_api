# from django.shortcuts import render
from rest_framework import generics
from .models import Joke
from .serializers import JokeSerializer


# def pick_random_object():
#     max_id = Joke.objects.all().aggregate(max_id=Max("id"))['max_id']
#     pk = random.randint(1, max_id)
#     return pk


class RandomJoke(generics.ListAPIView):
    queryset = Joke.objects.all().filter(id=1)  # TODO: pick_random_object()
    serializer_class = JokeSerializer
