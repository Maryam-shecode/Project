
from price import prices


def create_bill(order):

    bill = {}
    subtotal = 0
    for item, quantity in order.items():

        unit_price = prices[item]
        item_total = quantity * unit_price

        bill[item] = {
            "quantity": quantity,
            "unit_price": unit_price,
            "total": item_total
        }

        subtotal += item_total

    if subtotal >= 1000:
        discount = subtotal * 0.05
    else:
        discount = 0

    vat = (subtotal - discount) * 0.02
    final_amount = subtotal - discount + vat

    return bill, subtotal, discount, vat, final_amount


def display_bill(bill, subtotal, discount, vat, final_amount):

    print("\n================ GROCERY SHOP BILL ================")

    print(
        f"{'Item':<12}"
        f"{'Quantity':>10}"
        f"{'Unit Price':>14}"
        f"{'Total':>12}"
    )

    print("-" * 50)

    # Display each product
    for item, details in bill.items():

        print(
            f"{item:<12}"
            f"{details['quantity']:>10}"
            f"{details['unit_price']:>14.2f}"
            f"{details['total']:>12.2f}"
        )

    print("-" * 50)

    print(f"{'Subtotal:':<35} Tk {subtotal:>9.2f}")
    print(f"{'Discount (5% if eligible):':<35} Tk {discount:>9.2f}")
    print(f"{'VAT (2%):':<35} Tk {vat:>9.2f}")

    print("-" * 50)

    print(f"{'Final amount:':<35} Tk {final_amount:>9.2f}")

    print("=" * 50)
