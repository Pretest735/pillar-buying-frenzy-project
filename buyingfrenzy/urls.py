from django.urls import path
from .views import *
urlpatterns = [
    path('restaurants/', RestaurantList.as_view()),
    path('menus/', MenuList.as_view()),
    path('open-hours/', OpenHoursList.as_view()),
    path('users/', UserList.as_view()),
    path('purchase-history/', PurchaseHistoryList.as_view()),

]