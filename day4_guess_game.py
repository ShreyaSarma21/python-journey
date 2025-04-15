secret_num  = 7

for attempt in range(5):
    guess = int(input("Guess the number(1-10):"))
    
    if guess == secret_num:
        print("You win!")
        break
    else:
        print("Try again")
else:
    print("Out of attempts. The number was", secret_num)




