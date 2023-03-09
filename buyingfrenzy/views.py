from django.shortcuts import render
from rest_framework.views import generics, APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from datetime import datetime
from dateutil import parser
from .models import *
from .serializers import *

# Create your views here.

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OpenHoursList(generics.ListAPIView):
    queryset = OpenHours.objects.all()
    serializer_class = OpenHoursSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PurchaseHistoryList(generics.ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer

class RestaurantQueryList(APIView):
    def get_object(self, name):
        try:
            Restaurant.objects.get(restaurant_name=name)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_name, format=None):
            restaurant = self.get_object(restaurant_name)
            return Response(restaurant)
        
class MenuQueryList(APIView):
    def get_object(self, name):
        try:
            Menu.objects.get(dish_name=name)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, dish_name, format=None):
            menu = self.get_object(dish_name)
            return Response(menu)

class RestaurantDateTimeQueryView(APIView):
    def get(self, request, format=None):
        date = request.data.date
        time = request.time
        # get day of the week
        week_days = ['Sun', 'Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat']
        day_num = datetime.strftime(parser.parse(date), '%w')
        query_day = week_days[int(day_num)]
        
        # need to run a join query
        # select * from restaurant join on (openhours.restaurant_id == restaurant.id) where day=day and time >= open and time <= close

        results = OpenHours.objects.filter(day=query_day, opening_hour__lte=time, closing_hour__gte=time)
        open_restaurants = []
        for temp in results:
            open_restaurants.append(temp.restaurant)

        serializer = RestaurantSerializer(open_restaurants, many=True)
        return Response(serializer.data)

class DishPriceQueryList(APIView):
    def get(self, request):
        print(request)
        min_price = request.data.min_price
        max_price = request.data.max_price
        query_type = request.data.query_type
        x = request.data.x

        # run more or less query
        # first get all menus within price range and join them based on restaurant_id
        results = Menu.objects.filter(price__gte=min_price, price__lte=max_price)
        restaurant_count_dictionary = {}
        restaurant_list = []
        for menu in results:
            if menu.restaurant.restaurant_name in restaurant_count_dictionary.keys():
                restaurant_count_dictionary[menu.restaurant.restaurant_name] += 1
            else: 
                restaurant_count_dictionary[menu.restaurant.restaurant_name] = 0

        for k,v in restaurant_count_dictionary:
            if query_type == 'more':
                if v > x:
                    restaurant_list.append(k)
                
            if query_type == 'more':
                if v < x:
                    restaurant_list.append(k)
        restaurant_list = sorted(restaurant_list, key=lambda res: res['restaurant_name'])
        serializer = RestaurantSerializer(restaurant_list, many=True)
        return Response(serializer.data)

class UserPurchase(APIView):
    def post(self, request, user_id, format=None):
        query_dish_name = request.data.dish_name
        query_restaurant_name = request.data.restaurant_name

        # get user, menu and restaurant
        user = User.objects.get(id=user_id)
        orders = Menu.objects.filter(dish_name=query_dish_name)
        
        ordered_menu={}
        for order in orders:
            if order.restaurant.restaurant_name==query_restaurant_name:
                ordered_menu=order
        
        if ordered_menu:
            # check and update user cash balance
            if user.cash_balance >= ordered_menu.price:
                user.cash_balance-= ordered_menu.price
                user.save()

                #update restaurant cash balance
                restaurant=ordered_menu.restaurant
                restaurant.cash_balance+= ordered_menu.price
                restaurant.save()

                # update insert purchase history
                purchase_history=PurchaseHistory()
                purchase_history.dish_name=ordered_menu
                purchase_history.restaurant=restaurant
                purchase_history.user=user
                purchase_history.transaction_amount=ordered_menu.price
                purchase_history.transaction_date=datetime.utcnow()
                purchase_history.save()
                serializer=PurchaseHistorySerializer(purchase_history)
                return Response(serializer.data)

            else:
                message="User balance is insufficient for order"
                return Response(message)
        else:
            message="Menu unavailable"
            return Response(message)


            
        
