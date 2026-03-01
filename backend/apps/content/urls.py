from django.urls import path

from . import views


urlpatterns = [
    path("sets/", views.word_sets),
    path("sets/<str:set_key>/words/", views.set_words),
]

