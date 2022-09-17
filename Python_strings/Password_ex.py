#ask user to enter password
#if passford does not any uppercase or does not have any lower case print Fales, otherwise, print TRue


#password hsould have upper case and lower case
# "password" will be equal to its lower case

print("enter password in upper and lower case")
password=input()
is_there_uppercase= password!=password.lower()
#PASSWORD" will be equal to its upper case version
#if the password is not equal to its upper case version

is_there_lowercase=password!=password.upper()
is_valid_pass=is_there_lowercase and is_there_uppercase
print("your password is valid", is_valid_pass)



