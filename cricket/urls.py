from django.urls import path
from .views import cricket_data

urlpatterns = [
    path('cricket/', cricket_data, name='cricket_data'),
]
