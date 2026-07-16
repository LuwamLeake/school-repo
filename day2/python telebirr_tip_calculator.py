# Store the bill total and number of people
bill_total = 1200
people = 4

# List of names
names = ["Abel", "Sara", "Mahi", "John"]

# Function
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

# Calculate each person's share
share = split_bill(bill_total, people)

# Print the result
for name in names:
    print (f"{name} should pay {share:.2f} ETB")