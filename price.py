
# Available products and their unit prices

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
    print("\nAVAILABLE PRODUCTS")
    print("------------------------------")

    for product, price in prices.items():
        print(f"{product:<12} Tk {price:.2f}")

    print("------------------------------")
