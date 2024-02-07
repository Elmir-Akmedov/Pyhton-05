print("Creating Pyramid".center(20))
rows = int(input(">> "))

def create_left(x):
    print(" " * (rows-x), end="")
    print("*" * x, end="")


def create_right(x):
    print("*" * (x-1))


def create_pyramid(rows):
    for x in range(1, rows+1):
        create_left(x)
        create_right(x)
        

if __name__ == "__main__":
    rows = int(input(">> "))
    create_pyramid(rows)
