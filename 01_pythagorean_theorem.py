# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# Consider a right angled triangle whose two small sides are AB and AC. To find the hypotenuse,BC, input the two sides.

import math
AB = float(input("Enter the length of side AB: "))
AC = float(input("Enter the length of side AC: "))

#BC = (AB**2 + AC**2)**0.5    #Can be used if not importing math
BC = math.sqrt(AB**2 + AC**2)

print(f"The length of side BC is: {BC}")

Solution
Enter the length of side AB: 34
Enter the length of side AC: 42
The length of side BC is: 54.037024344425184
