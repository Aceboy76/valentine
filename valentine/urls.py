from django.urls import path

from .views import ValentineView, FormView

urlpatterns = [
    path("", ValentineView.as_view(), name="home"),
    path("form/", FormView.as_view(), name="form"),
]
