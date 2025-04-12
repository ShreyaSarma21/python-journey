import getpass  # used to hide password input in terminal

# Set the correct credentials
correct_username = "shreya"
correct_password = "python123"

# Allow user up to 3 login attempts
for attempt in range(3):
    print(f"\nAttempt {attempt + 1} of 3")

    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()

    if username == correct_username and password == correct_password:
        print("Login successful. Welcome, Shreya!")
        break
    else:
        print("Invalid credentials.")

# If the user fails 3 times
else:
    print("\n Too many failed attempts. Access denied.")

