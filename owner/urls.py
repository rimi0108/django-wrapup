from django.urls import path

from owner.views import OwnerView

urlpatterns = [
    path("", OwnerView.as_view())
]