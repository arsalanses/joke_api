from django.urls import path
from .views import RandomJoke

urlpatterns = [
    path('random_joke/', RandomJoke.as_view()),
]
