from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.main, name='main'),
    path("upload/", views.upload, name='upload'),
    path("upload/rules/", views.rules, name='rules'),
    path("notifications/", views.notifications, name='notifications'),
    path("more/", views.more, name='more'),
    path("<str:category>/", views.jokes, name='jokes'),
]
