Write a program to solve this age-related riddle!
Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.

Code
# Anton's age
anton_age = 21

# Beth's age
beth_age = anton_age + 6

# Chen's age
chen_age = beth_age + 20

# Drew's age
drew_age = chen_age + anton_age

# Ethan's age
ethan_age = chen_age

# Print the ages of all friends
print("Anton's age:", anton_age)
print("Beth's age:", beth_age)
print("Chen's age:", chen_age)
print("Drew's age:", drew_age)
print("Ethan's age:", ethan_age)

Answer
Anton's age: 21
Beth's age: 27
Chen's age: 47
Drew's age: 68
Ethan's age: 47
