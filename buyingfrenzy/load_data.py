import json
from .models import *
from .serializers import *    
from datetime import datetime
from dateutil import parser

def load_restaurant_data():
    file = open("restaurant_with_menu.json")
    data = json.load(file)
    
    for restaurant in data:
        saved_restaurant = store_restaurant_data(restaurant.get("restaurantName"), restaurant.get("cashBalance"))
        populate_openhours_data(saved_restaurant, restaurant.get("openingHours"))

        menus = restaurant.get("menu")

        for menu in menus:
            store_menu_data(menu.get("dishName"), menu.get("price"), saved_restaurant)

def store_restaurant_data(name, balance):
    restaurant = Restaurant()
    restaurant.restaurant_name = name
    restaurant.balance = balance
    restaurant.save()
    return restaurant

week_days = ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun']
def populate_openhours_data(restaurant, openingHours):
    open_hours = OpenHours()
    open_hours.restaurant_name = restaurant
    opened_days = openingHours.split("/")
    
    for temp in opened_days:
        print(temp)
        day = temp.replace(' ', '')
        i = 0
        length = len(day)
        days = []
        # find the days first
        while i < length:
            if week_days.count(day[i: i+3]) != 0:
                # days with 3 letters Mon, Fri, Sat, Sun
                days.append(day[i:i+3])
                if day[i+3] == ',':
                    i += 4
                elif day[i+3].isdigit():
                    i += 3
                    break
            elif week_days.count(day[i:i+4]) != 0:
                # days with 4 letters Tues, Weds
                days.append(day[i:i+4])
                if day[i+4] == ',':
                    i += 5
                elif day[i+4].isdigit():
                    i += 4
                    break
            elif week_days.count(day[i:i+5]) != 0:
                # days with 5 letters Thurs
                days.append(day[i:i+5])
                if day[i+5] == ',':
                    i += 6
                elif day[i+5].isdigit():
                    i += 5
                    break
            else:
                break
        print(days)
        open_time = parser_time_hh_mm(day[i:].split('-')[0])
        close_time = parser_time_hh_mm(day[i:].split('-')[1])
        
        for day in days:
            store_openhour_data(day, open_time, close_time, restaurant)

    
def parser_time_hh_mm(t):
    print("Parser")
    print(parser.parse(t))
    return datetime.strftime(parser.parse(t), '%H:%M')

def store_openhour_data(day, open_time, close_time, restaurant):
    open_hours = OpenHours()
    open_hours.day = day
    open_hours.opening_hour = open_time
    open_hours.closing_hour = close_time
    open_hours.restaurant = restaurant
    open_hours.save()

def store_menu_data(dish_name, price, restaurant):
    menu = Menu()
    menu.dish_name = dish_name
    menu.price = price
    menu.restaurant = restaurant
    menu.save()


def load_user_purchase_history():
    file = open("users_with_purchase_history.json")
    data = json.load(file)

    for user_purchase_data in data:
        user_id = user_purchase_data.get("id")
        user_name = user_purchase_data.get("name")
        cash_balance = user_purchase_data.get("cashBalance")
        saved_user=store_user_data(user_id, user_name, cash_balance)

        purchase_history = user_purchase_data.get("purchaseHistory")
        for purchase in purchase_history:
            restaurant = Restaurant.objects.get(restaurant_name=purchase.get("restaurantName"))
            menu = Menu.objects.get(dish_name=purchase.get("dishName"))
            store_purchase_data(menu, restaurant, purchase.get("transactionAmount"), purchase.get("transactionDate"), saved_user)


def store_user_data(id, name, cash_balance):
    user = User()
    user.id = id
    user.name = name
    user.cash_balance = cash_balance
    user.save()
    return user

def store_purchase_data(dish_name, restaurant_name, transaction_amount, transaction_date, user_name):
    purchase_history = PurchaseHistory()
    purchase_history.dish_name = dish_name
    purchase_history.restaurant_name = restaurant_name
    purchase_history.transaction_amount = transaction_amount
    purchase_history.transaction_date = str(transaction_date).strip()
    purchase_history.user_name = user_name

load_restaurant_data()
load_user_purchase_history()