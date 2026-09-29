carrito = [
    {"item": "Pan", "price": 1.5},
    {"item": "Leche", "price": 2.0},
    {"item": "Huevos", "price": 3.25}
]

total = 0
for producto in carrito:
    total += producto["price"]
    print(producto["item"], "->", producto["price"])

print("Total:", total)