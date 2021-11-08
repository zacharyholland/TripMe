from django.urls import path
from.views import indexPageview, aboutPageView

urlpatterns = [
    path("", indexPageview, name="index"),
    path("about/", aboutPageView, name="about"),
]
