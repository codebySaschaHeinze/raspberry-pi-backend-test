from django.urls import path
from.views import fruits_list


urlpatterns = [
    path('', fruits_list),
]
