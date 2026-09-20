# my practice

warehouse = {
    "laptop": {"price": 45000, "stock": 5},
    "mouse": {"price": 1200, "stock": 20},
    "keyboard": {"price": 2500, "stock": 10},
    "monitor": {"price": 18000, "stock": 3},
}

discounted_item = {"laptop", "keyboard"}

cart = []

while True:
    product = input("select product or exit ")
    if product == "exit":
        break
    if product in warehouse:
        if warehouse[product]["stock"] > 0:
            warehouse[product]["stock"] -= 1
            cart.append(product)
            print("added to cart")
        else:
            print("the product is out of stock")
    else:
        print("product does not exist")

invoice = {}
total_price = 0

for item in set(cart):
    count = cart.count(item)
    unit_price = warehouse[item]["price"]
    item_total = unit_price * count

    if item in discounted_item:
        unit_price = unit_price * 0.9
        item_total = item_total * 0.9
        print(f"the {item} comes with a 10% discount")
    invoice[item] = {"quantity": count, "price": unit_price, "total price": item_total}
    total_price += item_total
print(f"your products invoice = {total_price} toman")

for key, value in invoice.items():
    print(
        f"{value['quantity']} {key} at the price of {value['price']} : {value['total price']}"
    )
if total_price > 100000:
    total_price -= 15000
    print("Good news!!! you gat 15000 toman discount")
    print(f"new invoice = {total_price} toman")
