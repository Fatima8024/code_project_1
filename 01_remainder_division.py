# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

dividend = float(input("Enter the dividend(the number to be divided): "))
divisor = float(input("Enter the divisor(the number to divide by): " ))

quotient = dividend / divisor
print(f"The quotient of {dividend} divided by {divisor} is {quotient}")

quotient1 = dividend // divisor
print(f"The quotient of {dividend} divided by {divisor} without remainder is {quotient1}")

remainder = dividend % divisor
print(f"The remainder of {dividend} divided by {divisor} is {remainder}")

Solution
Enter the dividend(the number to be divided): 9
Enter the divisor(the number to divide by): 5
The quotient of 9.0 divided by 5.0 is 1.8
The quotient of 9.0 divided by 5.0 without remainder is 1.0
The remainder of 9.0 divided by 5.0 is 4.0
