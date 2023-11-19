# Var name is left, value is right

price_per_item = 0.5
amount = 10

order_price = price_per_item * amount  # mult
print(order_price)

shipping_cost = 3.0

total_cost = order_price + shipping_cost  # add
print(total_cost)

voucher = 2.0
total_cost = total_cost - voucher  # sub
print(total_cost)

brothers_cost = total_cost / 2  # div
print(brothers_cost)
