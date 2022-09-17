

#using IN operator we can specify value is in the list or not



list=[1,2,3,4,5]

if 2 in list:
    print("2 is in the list")

if 11 in list:
    print("11 is in the list") #this line wont print because 11 isnot int he list



# not IN operator will check if specified value is not in the list (ieterable objects)


if 6 not in list:
    print("6 is not in the list")



   # ask user to enter random ### and check if the digit is present in our list or not
#if user enters present elements, print " you won a prize"

print("Enter number")
digit=int(input())
if digit in list:
    print("you have won aprize")
elif digit not in list:
    print("maybe next time")











