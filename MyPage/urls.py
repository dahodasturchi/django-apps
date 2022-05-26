from django.urls import path
from .views import MyPageView


urlpatterns = [
    path('', MyPageView, name='home')
]