dist_in_km = input("Enter your distance in km : ")
dist_in_km = float(dist_in_km)
dist_in_miles = dist_in_km * 0.621371
dist_in_miles = round(dist_in_miles,2)
print("Your distance in miles is :" + str(dist_in_miles))
# or
print(f"{dist_in_km} km is equal to {dist_in_miles} miles.")