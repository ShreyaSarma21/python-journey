# for loop basics 
for i in range(5):
    print("Python is awwsome!",i)

for letter in "shreya":
    print(letter)

for i in range(1,6):
    print(f"{i}. Stay consistent!")

# while loop basics
count = 1
while count <= 5:
    print("Looping",count)
    count += 1 #Make sure to apply this condition or else it will loop forever

counter = 1
while counter <= 3:
    print("While loop going on",counter)
    counter += 1

# Break example
for number in range(1, 10):
    if number == 5:
        break
    print("Number:", number)

# Continue example
for number in range(1, 6):
    #print("All numbers in range:",number)
    if number == 3:
        continue
    print("Number (skip 3):", number) 
    

