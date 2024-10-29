Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Prompt the user for the lengths of the three sides of the triangle
side1_str = input("Enter the length of the first side: ")
side2_str = input("Enter the length of the second side: ")
side3_str = input("Enter the length of the third side: ")

# Convert the input strings to numbers (float to handle potential decimal values)

side1 = float(side1_str)
side2 = float(side2_str)
side3 = float(side3_str)

# Calculate the perimeter
perimeter = side1 + side2 + side3

# Print the perimeter
print(f"The perimeter of the triangle is: {perimeter}")

Run
Enter the length of the first side: 4
Enter the length of the second side: 7
Enter the length of the third side: 9
The perimeter of the triangle is: 20.0
