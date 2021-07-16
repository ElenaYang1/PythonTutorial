lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. \
32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. \
29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""



while True:
    item = input("what would you like to buy? ")
    if item == "seat":
        customer_one_total += lovely_loveseat_price
        customer_one_itemization += lovely_loveseat_description
    elif item == "settee":
        customer_one_total += stylish_settee_price
        customer_one_itemization += stylish_settee_description
    elif item == "lamp":
        customer_one_total += luxurious_lamp_price
        customer_one_itemization += luxurious_lamp_description
    elif item == "done":
        customer_one_tax = customer_one_total * sales_tax
        customer_one_total += customer_one_tax
        print("Customer one items: {}".format(customer_one_itemization))
        print("Customer one total is: ${:.2f}".format(customer_one_total))
        break

    else:
        print('Sorry, item not available. Please choose "seat", "settee", or "lamp".')






