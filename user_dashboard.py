import getpass  # used to hide password input in terminal

correct_username = "shreya"
correct_password = "python123"

for attempt in range(3):
    print(f"\nAttempt {attempt + 1} of 3")

    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()

    if username == correct_username and password == correct_password:
        print("Login successful. Welcome, Shreya!")

        # Start dashboard after successful login
        age = int(input("How old are you? "))
        place = input("Where do you live? ")
        km = float(input("How many km did you travel today? "))

        miles = km * 0.621371
        miles = round(miles, 2)
        print(f"{km} km is equal to {miles} miles.")

        if age >= 18:
            print(f"You're an ADULT living in {place}.")
        else:
            print("You're a MINOR!")

        temp = int(input("What's the temperature outside? "))
        if temp > 30 or temp < 0:
            print("Extreme weather warning!")
        elif 18 <= temp <= 30:
            print("Perfect weather!")
        else:
            print("Might need a jacket.")

        break  # exit after successful login and dashboard
    else:
        print("Invalid credentials.")

# If the user fails 3 times
else:
    print("\nToo many failed attempts. Access denied.")
