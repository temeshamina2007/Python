customer_name = input("Enter customer name: ")
item1_name = input("Enter name of item one: ")
item1_price = float(input("Enter price of item one (KZT): "))
item2_name = input("Enter name of item two: ")
item2_price = float(input("Enter price of item two (KZT): "))
num_people = int(input("Enter number of people: "))
subtotal = item1_price + item2_price
tip = subtotal * 0.10
total = subtotal + tip
per_person = total / num_people
print("=" * 30)
print("          CAFE BILL")
print("-" * 30)
print(f"Customer: {customer_name}")
print(f"{item1_name}: {item1_price} KZT")
print(f"{item2_name}: {item2_price} KZT")
print(f"Subtotal: {subtotal} KZT")
print(f"Tip (10%): {tip} KZT")
print(f"Total: {total} KZT")
print(f"Per person: {per_person} KZT")
print("=" * 30)
print("Tip included:", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
print("=" * 30)