
from price import prices


def take_order():

    order = {}

    print("\nAVAILABLE PRODUCTS")
    for product, price in prices.items():
        print(f"{product:<12} Tk {price:.2f}")
    while True:
        try:
            number_of_entries = int(
                input("\nHow many order entries? ")
            )

            if number_of_entries > 0:
                break
            else:
                print("Please enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(number_of_entries):

        print(f"\nEnter product {i + 1}:")
        item = input("Product name: ").lower().strip()
        if item not in prices:
            print(f"{item} is not available.")
            continue
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                continue

        except ValueError:
            print("Please enter a valid whole-number quantity.")
            continue
        order[item] = order.get(item, 0) + quantity

    return order
