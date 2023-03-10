from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from datetime import datetime
from dateutil import parser
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.


class RestaurantList(APIView):
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuList(APIView):
    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetail(APIView):
    """
    Retrieve, update or delete a menu instance.
    """
    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menu = self.get_object(pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OpenHoursList(APIView):
    def get(self, request, format=None):
        open_hours = OpenHours.objects.all()
        serializer = OpenHoursSerializer(open_hours, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OpenHoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OpenHoursDetail(APIView):
    """
    Retrieve, update or delete a open_hour instance.
    """
    def get_object(self, pk):
        try:
            return OpenHours.objects.get(pk=pk)
        except OpenHours.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        open_hour = self.get_object(pk)
        serializer = OpenHoursSerializer(open_hour)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        open_hour = self.get_object(pk)
        serializer = OpenHoursSerializer(open_hour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        open_hour = self.get_object(pk)
        open_hour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PurchaseHistoryList(APIView):
    def get(self, request, format=None):
        purchase_historys = PurchaseHistory.objects.all()
        serializer = PurchaseHistorySerializer(purchase_historys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchaseHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseHistoryDetail(APIView):
    """
    Retrieve, update or delete a purchase_history instance.
    """
    def get_object(self, pk):
        try:
            return PurchaseHistory.objects.get(pk=pk)
        except PurchaseHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        purchase_history = self.get_object(pk)
        serializer = PurchaseHistorySerializer(purchase_history)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        purchase_history = self.get_object(pk)
        serializer = PurchaseHistorySerializer(purchase_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        purchase_history = self.get_object(pk)
        purchase_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RestaurantQueryList(APIView):
    def get_object(self, name):
        try:
            return Restaurant.objects.filter(restaurant_name=name)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
            restaurant_name = request.data.get("restaurant_name")
            restaurant = self.get_object(restaurant_name)
            serializer = RestaurantSerializer(restaurant, many=True)
            return Response(restaurant)
        
class MenuQueryList(APIView):
    def get_object(self, name):
        try:
            return Menu.objects.filter(dish_name=name)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        dish_name = request.data.get("dish_name")
        menu = self.get_object(dish_name)
        serializer=MenuSerializer(menu, many=True)
        return Response(serializer.data)

class RestaurantDateTimeQueryView(APIView):
    def get(self, request, format=None):
        date = request.data.get("date")
        time = request.data.get("time")
        print(date, time)
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
        min_price = request.data.get("min_price")
        max_price = request.data.get("max_price")
        query_type = request.data.get("query_type")
        x = int(request.data.get("x"))

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
        query_dish_name = request.data.get("dish_name")
        query_restaurant_name = request.data.get("restaurant_name")

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


            
        
