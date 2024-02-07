data = {}
with open("stock_data.txt") as stock_data:
    for line in stock_data.readlines():
        key, value =line.strip().split(" - ")
        data[key] = int(value)

for item, price in enumerate(data.items, start=1):
    obj, price = item
    print(f"{item}, {obj}: {price}")
else:
    print("choose item:")

