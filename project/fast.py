import time
data = {
    "tv": {
        "id": 1,
        "price": 1900,
        "count": 17
    },
    "monitor": {
        "id": 2,
        "price": 800,
        "count": 63
    },
    "computer": {
        "id": 3,
        "price": 3900,
        "count": 1
    },
}
start = time.time()
total_price = 0
for obj in data:
    total_price += data[obj]["price"] * data[obj]["count"]
end = time.time()
print(start, end ,end - start)
print(total_price)