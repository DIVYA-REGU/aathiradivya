from collections import OrderedDict
num_items = int(input())
item_prices = OrderedDict()
for _ in range(num_items):
    item_name, price = input().rsplit(' ', 1)
    price = int(price)
    if item_name in item_prices:
        item_prices[item_name] += price
    else:
        item_prices[item_name] = price
for item_name, price in item_prices.items():
    print(item_name, price)
