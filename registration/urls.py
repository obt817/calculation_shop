from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import indexView


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("", login_required(indexView.as_view()), name="index"),
]
