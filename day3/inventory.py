# inventory.py

stock = {}

# Read stock from file
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)
except FileNotFoundError:
    print("No stock file yet — starting empty.")

# Function to adjust stock
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount
    print(f"{item} updated. New quantity: {stock[item]}")

# Example transactions
adjust("Paracetamol", 5)
adjust("Amoxicillin", -3)
adjust("Vitamin C", 20)

# Display low-stock items
print("\nLow Stock Items:")
low_stock = [item for item, qty in stock.items() if qty < 10]

if low_stock:
    for item in low_stock:
        print(f"- {item}: {stock[item]}")
else:
    print("No low-stock items.")

# Save updated stock back to file
with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nStock has been saved successfully.")