my_dict = {
    "ə": "e",
    "ç": "c",
    "ş": "s",
    "ğ": "g",
    "ö": "o",
    "ü": "u",
    "ı": "i",
}

def generate_slug(name):
    words = my_dict.keys()
    name = "-".join(name)
    for char in words:
        if char in name:
            name = name.replace(char, my_dict[char])
    print(name)

if __name__ == "__main__":
    user_string = input(">> ").lower().split()
    generate_slug(user_string)