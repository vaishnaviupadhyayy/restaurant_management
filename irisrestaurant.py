import time
menuitems = {
    "1": {"item": "Paneer Lababdar", "price": 260.00},
    "2": {"item": "Mushroom Masala", "price": 250.00},
    "3": {"item": "Dal Makhani", "price": 150.00},
    "4": {"item": "Aloo Gobi Dry", "price": 210.00},
    "5": {"item": "Veg Samosa (2 pcs)", "price": 150.00},
    "6": {"item": "Naan (2pcs)", "price": 50.00},
    "7": {"item": "Margarita Pizza(Regular)", "price": 320.00},
    "8": {"item": "Alfredo Pasta", "price": 350.00},
    "9": {"item": "Arrabiatta Pasta", "price": 300.00},
    "10": {"item": "Manchow Soup", "price": 220.00},
    "11": {"item": "Schezwan Noodles", "price": 200.00},
    "12": {"item": "Manchurian Dry/Gravy", "price": 250.00},
    "13": {"item": "Veg Fried Rice", "price": 200.00},
    "14": {"item": "Spring Rolls (8 pcs)", "price": 300.00},
    "15": {"item": "Indian combo", "price": 250.00},
    "16": {"item": "Tiramisu", "price": 320.00},
    "17": {"item": "Choco Lava Cake", "price": 280.00},
    "18": {"item": "Gulab Jamun (2 pcs)", "price": 160.00},
    "19": {"item": "Rasgulla (2 pcs)", "price": 160.00},
    "20": {"item": "Cheesecake Slice", "price": 350.00},
    "21": {"item": "Mint Mojito", "price": 90.00},
    "22": {"item": "Kitkat/Oreo Shake", "price": 80.00},
    "23": {"item": "Bottled Water (1L)", "price": 60.00}
}
tax = 0.08 

def display_menu():
    print("\n" + "="*60)
    print("      WELCOME TO IRIS RESTAURANT       ")
    print("="*60)
    print("Code | Item                           | Price (Rs.)")
    print("-" * 60)
    
    for code, details in menuitems.items():
        print(f"{code:<4} | {details['item']:<25}     | Rs.{details['price']:<5.2f}")
    
    print("-" * 60)
    print("Enter 'DONE' to finish ordering.")
    print("="*60)

def take_order():
    order = []
    while True:
        choice = input("Enter Menu Code (1-23) or 'DONE': ").upper()
        if choice == 'DONE':
            break
        if choice in menuitems:
            while True:
                try:
                    quantity = int(input("How many would you like? "))
                    if quantity > 0:
                        order.append({
                            "code": choice,
                            "item": menuitems[choice]['item'],
                            "price": menuitems[choice]['price'],
                            "quantity": quantity
                        })
                        print("Added to your order.")
                        break
                    else:
                        print("Quantity must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a number for the quantity.")
        else:
            print("Invalid menu code. Please try again or enter 'DONE'.")
    return order

def generate_bill(order):
    if not order:
        print("\nThank you for visiting Iris Restaurant!")
        return

    subtotal = 0.0
    print("\n" + "="*60)
    print("           IRIS RESTAURANT BILL               ")
    print("="*60)
    print("Qty | Item                        | Price  | Total (Rs.)")
    print("-" * 60)
    
    for item in order:
        line_total = item['price'] * item['quantity']
        subtotal += line_total
        print(f"{item['quantity']:<3} | {item['item']:<20}| Rs.{item['price']:<5.2f} | Rs.{line_total:<5.2f}")
    tax_amount = subtotal * tax
    grand_total = subtotal + tax_amount
    
    print("-" * 60)
    print(f"{'Subtotal:':<40} Rs.{subtotal:<5.2f}")
    print(f"{f'Sales Tax ({int(tax * 100)}%):':<40} Rs.{tax_amount:<5.2f}")
    print("=" * 60)
    print(f"{'GRAND TOTAL:':<40} Rs.{grand_total:<5.2f}")
    print("=" * 60)
    print("\nThank you for dining at Iris Restaurant! Have a great day!")

def run_restaurant_system():
    print("Welcome to Iris Restaurant! We're ready to take your order.") # Updated Restaurant Name
    display_menu()
    customer_order = take_order()
    generate_bill(customer_order)

if __name__ == "__main__":
    run_restaurant_system()
