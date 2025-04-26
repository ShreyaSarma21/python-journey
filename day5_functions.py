#Function that prints a greeting
def greet_user(name):
    print(f"Hello,{name}!")

#Function that adds 2 numbers
def add(a,b):
    return a+b

#Function that checks if a number is even
def is_even(number):
    return number % 2 == 0

# Call the functions
greet_user("Aastha")
print("Sum is:",add(6,7))

num = 6
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")