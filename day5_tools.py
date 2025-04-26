# Function to convert kilometers to miles
def convert_km_to_miles(km):
    miles = km * 0.621371
    return round(miles, 2)

# Function to check age group
def check_age_group(age):
    if age >= 18:
        return "adult"
    else:
        return "minor"

# Function to validate login
def validate_login(username, password):
    correct_username = "shreya"
    correct_password = "python123"
    return username.lower() == correct_username and password == correct_password

# Main function
def main():
    print("Welcome to the Utility Dashboard")
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not validate_login(username, password):
        print("Invalid credentials. Exiting.")
        return

    print("Login successful!")

    age = int(input("Enter your age: "))
    group = check_age_group(age)
    print(f"You are an {group}.")

    km = float(input("Enter distance in kilometers: "))
    miles = convert_km_to_miles(km)
    print(f"{km} km is equal to {miles} miles.")

# Run main only if this file is executed directly
if __name__ == "__main__":
    main()
