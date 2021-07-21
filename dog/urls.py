from django.urls import path

from dog.views import DogView

urlpatterns = [
    path("", DogView.as_view())
]