#Joseph Everden
#01/10/14
#Temperature

water_temp = float(input("Enter the temperature of your water: "))
if water_temp >= 100:
    print("Your water is boiling!")
if water_temp > 0 and water_temp < 100:
    print("Your water is neither boling or frozen.")
if water_temp <= 0:
    print("Your water is frozen!")
