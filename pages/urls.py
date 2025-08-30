from django.urls import path
from .views import HomePageView, AboutpageView

urlpatterns = [
    path('josefino/', HomePageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
]
    