# Comparison operators
print(42 == 42)    # True
print(42 == 99)    # False
print(2 != 3)      # True
print(2 != 2)      # False


# if statement
name = 'Alice'
if name == 'Alice':
    print('Hi, Alice')


    username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret":
    print("Access granted")
else:
    print("Access denied")

    age = input(int("Enter your age: "))

if age >= 13 and age <= 19:
    print("You are a teenager")
elif age < 13:
    print("You are a child")
else:
    print("You are an adult")