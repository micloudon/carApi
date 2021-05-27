from django.urls import path
from .views import home, api, car_list, car_detail, car_detail_make, car_detail_model, car_detail_year

urlpatterns = [
    path('', home),
    path('api/', api),
    path('api/all', car_list),
    path('api/<int:pk>/', car_detail),
    path('api/<str:make>/', car_detail_make),
    path('api/<str:make>/<str:model>/', car_detail_model),
    path('api/<str:make>/<str:model>/<int:year>', car_detail_year),

]