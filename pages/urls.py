from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('josefino/', HomePageView.as_view(), name='home'),
]
    