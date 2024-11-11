# Technewjeans Exercise 7

def get_order_details():
    # Collects the order details from the user, including product name, price, and quantity.

    # TODO: (Clarence Villas)
    details = []
    while True:
        product_name = input("Enter product name: ")
        price = float (input("Enter price: "))
        quantity = int (input("Enter quantity: "))

        order = {
            'product_name': product_name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        details.append(order)
	
        add_more = input("Do you want to add another item? (y-yes/n-no): ")
        if add_more != 'y':
            break
    return details
def get_customer_info():
    # Collects the customer information including name and senior ID number.

    # TODO: (Krislyn Francisoo)
    name = input("Enter customer name: ")
    is_senior = input("Welcome! Are you a senior citizen? (leave it blank if not senior citizen): ")

    if is_senior == 'yes' or is_senior == 'y':
        # Collecting customer name
        name = input("Enter your name: ")
        # Collecting senior ID number
        is_senior = input("Enter your senior ID number: ")

        customer_info = {
            "name": name,
            "is_senior": is_senior
        }
    return {"name": name, "is_senior": is_senior}

def calculate_total (details):
    # Calculates the grand total from the list of details.

    # TODO: (Member 3)
    grand_total = 0

    for order in details:
        grand_total += order['total']
    
    return grand_total
def apply_discount (grand_total, is_senior):
    # Applies a 10% discount to the grand total if the senior ID is provided.

    # TODO: (Member 4)
    if is_senior:
        return grand_total * 0.9 # 10% discount
    return grand_total

def display_summary (details, customer_info, final_total):
    # Displays the summary of the order including customer information and total amount.

    # TODO: (Member 5)
    print("\nOrder Summary:")
    print(f"Customer Name: {customer_info['name']}")
    print(f"Senior ID No.: {customer_info['is_senior'] if customer_info['is_senior'] else 'N/A'}")
    print("\nDetails:")
    for order in details:
        print(f"{order['product_name']}, ₱{order['price']:.2f}, Quantity: {order['quantity']}, Total: ₱{order['total']:.2f}")
    print(f"\nGrand Total: ₱{final_total:.2f}")

# Main program execution
def main():
    details = get_order_details()
    customer_info = get_customer_info()
    grand_total = calculate_total(details)
    final_total = apply_discount(grand_total, customer_info['is_senior'])
    display_summary(details, customer_info, final_total)

if __name__ == "__main__":
    main()
