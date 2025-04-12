# Basic if-else
age = int(input("enter your age: "))

if age >= 18 :
    print("You're an ADULT !")
else :
    print("You're a MINOR !")

# Multiple conditions
score = int(input("Enter your test score : "))

if score>= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 55:
    print("Grade C")
else:
    print("Grade F")

#Using 'and' and 'or'
temp = int(input("What's the temperature outside? "))

if temp>30 or temp<0:
    print("Extreme weather warning! ")
elif 18 <= temp <= 30:
    print("Perfect weather!")
else:
    print("Might need a jacket.")