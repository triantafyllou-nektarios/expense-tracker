expenses = []
print("=== Personal Expense Tracker ===")

while True:
    description = input("What did you buy? ")

    try:
        amount = float(input("What is the expense amount? "))

    except ValueError:
        print("Invalid amount")
        continue

    if amount <= 0:
        print("Invalid amount")
        continue

    category = input("What category does this expense belong to? ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    answer = input("Do you want to add another expense? ")

    while answer.lower() != "yes" and answer.lower() != "no":
        print("Please answer yes or no")
        answer = input("Do you want to add another expense? ")

    if answer.lower() == "no":
        break


print("Your expenses:")

total = 0

for expense in expenses:
    print(
        f"{expense['description']} - "
        f"€{expense['amount']:.2f} - "
        f"{expense['category']}"
    )

    total = total + expense["amount"]


print(f"Total expenses: €{total:.2f}")


category_to_find = input("Which category do you want to see? ")

print("Filtered expenses:")

category_total = 0

for expense in expenses:
    if expense["category"].lower() == category_to_find.lower():
        print(
            f"{expense['description']} - "
            f"€{expense['amount']:.2f} - "
            f"{expense['category']}"
        )

        category_total = category_total + expense["amount"]


print(f"Total for {category_to_find}: €{category_total:.2f}")