
from curses.ascii import islower


s="Python"
print(s.islower())
# false because its True oonly if it has all lower case

print(s.lower().islower())


s.upper()#usong methods in string will not affect the original value of string
print(s.isupper()) #FALSE

#ask user to enter their name in uppercase
#if they didnt enter in uppercase, printFalse

print("enter your name in uppercase")
first_name=input()
print(first_name.isupper())







