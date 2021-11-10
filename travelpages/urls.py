from django.urls import path
from.views import indexPageview, aboutPageView

urlpatterns = [
    path("about/<str:trip_name>/<int:trip_length>", aboutPageView, name="about"),
    path("", indexPageview, name="index"),
]
