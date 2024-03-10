while True:
    print("Who are you")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (it is fish)")
    password = input()
    if password == "swordfish":
        break
print("Access granted")