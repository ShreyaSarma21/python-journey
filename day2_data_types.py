# Integers and Floats
x = 10   #int
y = 3.14 #float

# Strings
name = "Shreya"
greeting = "Hellooo," + name

# Booleans
is_coding =  True

# Type Checking
print(type(x))
print(type(name))

# Type Casting
num_str = "42"
print(int(num_str) + 1)

# Input + Conversion
age = input("enter your age: ") # input is always a string
age = int(age)
print(f"Next year you'll be {age + 1}")

# Mixing types (causes error if not cast)
# print("You are " + age + " years old") ❌
print("You are " + str(age) + " years old")  # ✅


