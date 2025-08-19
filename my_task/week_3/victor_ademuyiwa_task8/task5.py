# Store Inventory Update
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Asking user for the item they want to buy and the quantity they need
item = input(f"Enter the item you want to buy\nAvailable items: {", ".join(store.keys())}: ").title()
quantity = int(input(f"Enter the quantity of {item} you want to buy\nAvailable quantity is {store.get(item)}: "))

print(f"Before purchase: {store}")

# reducing the quantity in the store
store[item] -= quantity
print(f"After purchase: {store}")