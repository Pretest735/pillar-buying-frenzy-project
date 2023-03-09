from django.urls import path
from .views import *
urlpatterns = [
    path('restaurants/', RestaurantList.as_view()),
    path('menus/', MenuList.as_view()),
    path('open-hours/', OpenHoursList.as_view()),
    path('users/', UserList.as_view()),
    path('purchase-history/', PurchaseHistoryList.as_view()),
    path('restaurants/<restaurant_name>', RestaurantQueryList.as_view()),
    path('restaurants/date-time/', RestaurantDateTimeQueryView.as_view()),
    path('menus/<dish_name>', MenuQueryList.as_view()),
    path('menus/price-range', DishPriceQueryList.as_view()),
    path('purchase/<user_id>/transaction', UserPurchase.as_view())

]