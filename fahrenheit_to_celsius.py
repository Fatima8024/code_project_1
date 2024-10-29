# prompt: Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# Prompt the user for a temperature in Fahrenheit
fahrenheit_str = input("Enter the temperature in Fahrenheit: ")

# Convert the input to a float
fahrenheit = float(fahrenheit_str)

celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} degrees in celsius is {celsius} ")

Answer
Enter the temperature in Fahrenheit: 43
43.0 degrees in celsius is 6.111111111111111 
