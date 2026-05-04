"""
Inputs:
-  age
-  day of the week
-  height
-  VIP
-  signed waiver
-  parent present

Processes:
-  Use the variables to identify which rides are available

Ouputs:
-  A list of rides

"""
# Inputs
age = int(input("Age: "))
day_of_week = input("Day of week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP? yes/no ").lower()
signed_waiver = input("Signed waiver? yes/no ").lower()
parent_present = input("Parent present? yes/no ").lower()

# Mega Drop
"""if age >= 14 and signed_waiver == "yes" and (height >= 54 or (vip == "yes" and height >= 50)):
    print("Mega drop")"""

ride_found = False

if age >= 14 and signed_waiver == "yes":
    if height >= 54:
        print("Mega drop")
        ride_found = True
    elif height >= 50 and vip == "yes":
        print("Mega drop")
        ride_found = True

# Thunderbolt
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")
    ride_found = True

# Kiddie coaster
if age > 8 or parent_present == "yes":
    print("Kiddie coaster")
    ride_found = True

if ride_found == False:
    print("No ride found.")