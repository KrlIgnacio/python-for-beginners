# conversor de peso
# kg <-> lb

# your weigth
# (K)kg or (L)lb

weigth = float(input("Your Weigth: ")) 
conversion = str(input("(K)g or (L)bs: "))

if conversion.upper() == "K":
    converted = weigth / 2.20462
    print(f"Weigth in Kgs: {converted}")
elif conversion.upper() == "L":
    converted = weigth * 2.20462
    print(f"Weigth in Lbs: {converted}")
else:
    print("Enter a valid string! ")