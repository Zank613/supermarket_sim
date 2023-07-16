from collections import Counter
import random

# Dictionary containing information about the supermarket goods
supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}

# List of goods available in the supermarket
list_of_goods = [
    "milk", "biscuits", "butter", "cheese", "bread",
    "cookies", "yogurt", "apples", "oranges", "bananas"
]

def random_shoplist(list_of_goods):
    """Generates a random shopping list based on the given goods."""
    random_length = len(list_of_goods)
    shopping_list = random.choices(list_of_goods, k=random_length)
    return shopping_list

# Variables to store the shopping lists for each customer
customer1 = customer2 = customer3 = customer4 = None

# Loop to generate shopping lists for four customers
count = 0
while count < 4:
    shopping_list = random_shoplist(list_of_goods)
    counts = dict(Counter(shopping_list))
    duplicates = {key: value for key, value in counts.items() if value > 1}

    # Assigning shopping lists to customer variables
    if customer1 is None:
        customer1 = duplicates
    elif customer2 is None:
        customer2 = duplicates
    elif customer3 is None:
        customer3 = duplicates
    elif customer4 is None:
        customer4 = duplicates
    count += 1

# List to store the calculated receipts for each customer
receipts = [{} for _ in range(4)]

# Iterating over each item in the supermarket
for item in supermarket:
    quantity = supermarket[item]["quantity"]
    price = supermarket[item]["price"]

    # Calculating receipts for each customer
    for i, customer in enumerate([customer1, customer2, customer3, customer4]):
        if item in customer:
            customer_quantity = customer[item]
            customer_receipt = price * customer_quantity
            receipts[i][item] = customer_receipt
            quantity -= customer_quantity

    # Printing the remaining quantities of each item in the supermarket
    print(f"{quantity} are left from item {item}")

# Printing the total cost and individual costs for each customer
for i, receipt in enumerate(receipts, start=1):
    total = sum(receipt.values())
    print(f"Customer {i} paid a total of {total:.2f}.")
    for item, amount in receipt.items():
        print(f"    {item}: {amount:.2f}")
