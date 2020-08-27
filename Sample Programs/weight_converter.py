#Weight converter

weight = int(input("Weight:"))

#getting the scale
scale = input("(L)bs or (K)g:")

#if condition for the scale

#Converting from lbs to kilo
if scale.upper() == "L":
    kgs = weight * 0.45
    print(f"You are {kgs}kilo")

#Converting from kilo to lbs
elif scale.upper() == "K":
    lbs = weight / 0.45
    print(f"You are {lbs} lbs")
