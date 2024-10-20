def addressval(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("invalid")
    elif (at == -1):
        print("invalid")
    else:
        print("Valid")
x = input("Give a valid address:")
addressval(x)