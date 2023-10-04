import math

print("\tWelcome To The Triangle Solver App")

#Input data
fstleg = float(input("\n\tWhat is the first leg of the triangle: "))
scndleg = float(input("\tWhat is the second leg of the triangle: "))

#Hypotenus Calculation
hypotenus = math.sqrt((fstleg**2) + (scndleg**2))
hypotenus = round(hypotenus,3)

#Area calculation
ar_triangle = 0.5*fstleg*scndleg
ar_triangle = round(ar_triangle,3)

#Display results
print("\n\tFor a triangle with legs of {} and {} the hypotenus is {}".format(fstleg , scndleg , hypotenus))
print("\tFor a triangle with legs of {} and {} the area is {}".format(fstleg , scndleg , ar_triangle))
