from django.urls import path
from .views import home, api, car_list, car_detail

urlpatterns = [
    path('', home),
    path('api/', api),
    path('api/all', car_list),
    path('api/<int:pk>/', car_detail)

]