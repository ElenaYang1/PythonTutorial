def generate_trip_instructions(location):
    print("looks like you're planning a trip to visit {}".format(location))
    print ("you could take the subway to get to {}".format(location))
generate_trip_instructions("eglinton mall")

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time = 7):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time
    coupon_discount = 10
    hotel_total -= coupon_discount
    total = car_rental_total + hotel_total + plane_ticket_price
    print(total)

# trip_planner(destiantion1, destination2, [destination3])
def trip_planner(destination1, destination2, destination3 = "home"):
    print("here's what your trip will look like:")
    print("first, we'll stop at {}, then {}, and lastly{}".format(destination1, destination2, destination3))

trip_planner("Canada", "Mexico")
trip_planner("1", "2", "3")


# 1. built-in functions
# 2. user-defined functions

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

print(max(tshirt_price, shorts_price, mug_price, poster_price), min(tshirt_price, shorts_price, mug_price, poster_price))
print(round(tshirt_price, 1))

# variable scope

# top level (no indent)
budget = 1000 # scope = entire file

def func():
    print("the budget is {}".format(budget))

print(budget)
###
favourite_location = "Paris, Norway, Iceland"
def print_count_locations():
    print("There are 3 locations")

def show_favourite_locations():
    print("Your favourite locations are {}".format(favourite_location))

print_count_locations()
show_favourite_locations()

# returns
def calculate_exchange_rate(us_dollars, exchange_rate):
    amt = us_dollars * exchange_rate
    return amt

new_zealand_dollars = calculate_exchange_rate(100, 1.4)
