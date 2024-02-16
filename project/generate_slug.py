my_dict = {
    "ə": "e",
    "ç": "c",
    "ş": "s",
    "ğ": "g",
    "ö": "o",
    "ü": "u",
    "ı": "i",
}

def modify_name(name):
    words = my_dict.keys()
    name = "-".join(name)
    for x in words:
        if x in name:
            name = name.replace(x, my_dict[x])
            print(name)

if __name__ == "__main__":
    user_string = input(">> ").lower().split()
    modify_name(user_string)