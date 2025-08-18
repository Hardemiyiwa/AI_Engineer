# Online Store Cart Calculation
# creating a list of item and a list of price
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]

# combing items and the price together
list_item_price = list(zip(items, prices))
print(list_item_price)

# Storing in key - value pair
items_price = {}
items_price.update({
    list_item_price[0][0]: list_item_price[0][1],
    list_item_price[1][0]: list_item_price[1][1],
    list_item_price[-1][0]: list_item_price[-1][1]
})

# Cart
cart_total = 0

# Adding the price of selected items to the cart


