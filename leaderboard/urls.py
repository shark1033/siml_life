from django.urls import path
from .views import index

urlpatterns = [

    path('', index), # '' means that it's a root route for the current app. ex: localhost/leaderboard/:8000

]