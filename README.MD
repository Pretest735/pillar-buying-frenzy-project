***Environment Setup:
1. The installed Python version is 3.10
2. After cloning the repository, cd to 'Pillar/' directory
3. Create a python virtual env
	- python3 -m venv pillar_env
	- source pillar_env/bin/activate
4. Install the following Dependencies
	- pip3 install django
	- pip3 install djangorestframework
	- pip3 install python-dateutil
	- pip3 install django-extensions

***Database Setup and ETL:
1. Default db.sqlite is used
2. We need to run the following commands to create the tables defined in models
	- python3 manage.py makemigration buyingfrenzy
	- python3 manage.py migrate
3. Next data load script is run with the following command to populate database
	- python3 manage.py runscript load_data --chdir /buyingfrenzy


***API Documentation:
List all restaurants that are open at a certain datetime
GET /restaurants/date-time
Params:
    date : "YYYY-MM-DD"
    time : "HH:MM"
Get all restaurants that are open on a day of the week, at a certain time

_GET /restaurants/restaurant
Param: restaurant_name
Search for restaurants with the restaurant name
**
_GET /menus/dish/
Param: dish_name_**
Search for menus with the dish name

_**GET /menus/price-range**
Params:
    max_price
    min_price 
    x
    query_type: 'more' or 'less'_
Get all restaurants that have more or less than x dishes that are within a price range, sorted alphabetically on restaurant name

_**POST /purchase/<user_id>/transaction**
params:
    restaurant_name: string
    dish_name: string
_    
process transactions when user buys a dish from a restaurant, adds to restaurant balance, subtracts from user balance, adds user purchase history.
covers checks for invalid conditions


***Run Server
1. Run the server with command "python3 manage.py runserver"
2. Then we can make requests using postman to 'http://127.0.0.1:8000/api/pillar-project/' above apis
