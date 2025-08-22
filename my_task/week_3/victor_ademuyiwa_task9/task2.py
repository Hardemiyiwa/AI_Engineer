# Shopping List Manager
shopping_list = []
for i in range(1, 4):
    # accepting user's shopping items
    items = input(f"Enter your number {i} shopping item: ")
    # Adding the user's item to the shopping list
    shopping_list.append(items)

# Displaying the shopping list
print(shopping_list)
print(f"shopping list: {", ".join(shopping_list)}")