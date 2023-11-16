import math
radius=float(input("enter a radius value"))
if radius>0:
    cir=2*math.pi*radius
    print("circumference is ",cir)
else:
    print("radius should be negative")
