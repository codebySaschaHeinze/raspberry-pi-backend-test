from django.urls import path
from.views import fruits_list, info


urlpatterns = [
    path('', fruits_list),
    path('info/', info, name='info'),
]
