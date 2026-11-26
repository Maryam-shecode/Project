
from order import take_order
from billing import create_bill, display_bill


def main():

    # Step 1: Take customer order
    order = take_order()

    # Step 2: Display combined order
    print("\nFINAL COMBINED ORDER")
    print(order)

    # Step 3: Check whether order is empty
    if not order:
        print("\nNo valid products were ordered.")
        return

    # Step 4: Calculate the bill
    bill, subtotal, discount, vat, final_amount = create_bill(order)

    # Step 5: Display the final bill
    display_bill(
        bill,
        subtotal,
        discount,
        vat,
        final_amount
    )


if __name__ == "__main__":
    main()
