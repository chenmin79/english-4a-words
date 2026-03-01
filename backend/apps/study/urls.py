from django.urls import path

from . import views


urlpatterns = [
    path("progress/<str:set_key>/", views.progress_by_set),
    path("progress/batch/", views.progress_batch),
    path("sessions/start/", views.session_start),
    path("sessions/end/", views.session_end),
]

