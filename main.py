prices = {
"rice": 75,
"oil": 185,
"sugar": 120,
"milk": 95,
"egg": 12,
"flour": 65,
"salt": 40,
"lentil": 130,
"potato": 45,
"onion": 80,
"tea": 250,
"coffee": 450,
"biscuit": 50,
"soap": 70,
"shampoo": 180
}
def display_products():
    print("Available Products")

    for item in prices:
        print(item, ":", prices[item])
