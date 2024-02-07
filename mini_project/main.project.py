import random
from datetime import datetime


company_data = []
user_data = []
payment_data = []

#Calculating time
current_date_and_time = datetime.now()

# Company info
company_name = "Great MMC"
company_location = "Bakı ş., Olimpiya küçəsi 6A, Gənclik Mall yaxınlığında"
company_data.extend([company_name, company_location])

# Get user info
print("Enter your full name:")
full_name = input(">> ").lower()
name, surname = full_name.split()
name = name.capitalize()
surname = surname.capitalize()
print("Enter your adress:")
adress = input(">> ")
print("Enter your email (with \"@gmail.com\"):")
email = input(">>  ")
user_data.extend([f"Name: {name}", f"Surname: {surname}", f"Email: {email}", f"Adress: {adress}"])

# Getting stock data
try:
    with open("stock_data.txt") as stock_data:
        data = dict(line.strip().split(" - ") for line in stock_data.readlines())
except FileNotFoundError:
    print("Stock file not found.")
    exit()

# Showing the stocks to the user
for num, (obj, price) in enumerate(data.items(), start=1):
    print(f"{num}. {obj}: {price}")
else:
    print(f"Choose an item(1,2,...,{len(data.keys())}):")
    try:
        user_item = int(input(">> "))
        item = list(data.keys())[user_item - 1]
    except IndexError:
        print("Invalid input.")
        exit()
    except ValueError:
        print("Invalid input.")
        exit()

# Getting the amount of the item
try:
    print(f"How many {item}'s you want to buy?")
    item_amount = int(input(">> "))
except ValueError:
    print("Invalid input.")
    exit()
#Creating payment data
total_cost = item_amount * int(data.get(item, 0))
payment_data.extend([f"Total: {total_cost}", f"Purchased Item: {item}", f"Quantity: {item_amount}"])

# Invoice generation
min_number = 10000000
max_number = 99999999
used_ids_file = "used_ids.txt"


# Generating new ID
def generate_unique_id():
    while True:
        random_id = random.randint(min_number, max_number)
        if not is_id_used(random_id):
            write_used_id(random_id)
            return random_id


# Checking if ID is used before.
def is_id_used(random_id):
    try:
        with open(used_ids_file, "r") as file:
            return str(random_id) in file.read()
    except FileNotFoundError:
        print("File not found")


# Writing the new ID if it is not in used IDs
def write_used_id(random_id):
    with open(used_ids_file, "a") as file:
        file.write(f"{name} {surname}={str(random_id)}\n")


user_unique_id = generate_unique_id()

# Extension
ext = "pdf"

#Creating shopping data
shopping_data = user_data + payment_data + company_data

#Creating lines
lines = []
max_line_length = max(len(line) for line in shopping_data)
lines.extend([f"{'-' * max_line_length}", "GREAT MMC".center(max_line_length)]) #line 1
lines.extend([f"{'-' * max_line_length}"]) #line 3
lines.extend([f"{data}".center(max_line_length) for data in user_data]) # user part
lines.extend([f"{'-' * max_line_length}"]) #line 8
lines.extend([f"{data}".center(max_line_length) for data in payment_data]) #Payment part
lines.extend([f"{'-' * max_line_length}"]) #line 12
lines.extend([f"{data}".center(max_line_length) for data in company_data]) #Company info part
lines.extend([f"{'-' * max_line_length}"]) #line 15
print(lines)

with open(f"{name}_{surname}_{user_unique_id}.{ext}", "w", encoding="utf-8") as invoice:
    invoice.writelines([f"{line}\n" for line in lines])




