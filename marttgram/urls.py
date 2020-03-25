"""marttgram URL Configuration"""

from django.urls import path
from django.http import HttpResponse

from marttgram import views


urlpatterns = [
    path('hello_word/', views.hello_word),
    path('get/', views.get),
    path('check_point/<str:name>/<int:age>/', views.check_point),

]
