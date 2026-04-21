# Online Shopping Cart with Discount

cart = []
total = 0

n = int(input("Enter number of items: "))

for i in range(n):
    print(f"\nItem {i+1}")
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    item_total = price * qty
    total += item_total

    cart.append((name, price, qty, item_total))

# Display Cart
print("\n----- Shopping Cart -----")
for item in cart:
    print(f"{item[0]} - ₹{item[1]} x {item[2]} = ₹{item[3]}")

print("\nTotal Amount: ₹", total)

# Discount Logic
discount = 0

if total > 5000:
    discount = total * 0.20   # 20% discount
elif total > 3000:
    discount = total * 0.15   # 15% discount
elif total > 1000:
    discount = total * 0.10   # 10% discount
else:
    discount = 0

final_amount = total - discount

# Output
print("\n----- Bill Summary -----")
print("Total Amount   : ₹", total)
print("Discount       : ₹", round(discount, 2))
print("Final Amount   : ₹", round(final_amount, 2))