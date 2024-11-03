# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Sentence_start : str = "Coding is fun.I learned to program and used Python to make "

adjective : str = input("Enter an adjective: ")
noun : str = input("Enter a noun: ")
verb : str = input("Enter a verb: ")

print(Sentence_start + adjective + " " + noun + " " + verb + ".")

Solution
Enter an adjective: cute
Enter a noun: sister
Enter a verb: singing
Coding is fun.I learned to program and used Python to make cute sister singing.
