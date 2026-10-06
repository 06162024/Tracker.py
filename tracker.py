# Laboratory 3 - Installment 3: The Tracker Does Math

print("=" * 40)
print("            EXPENSE TRACKER")
print("        Know where your money goes.")
print("=" * 40)
print()
print("MAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate ? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Ma. Cristina  |  Installment 3")