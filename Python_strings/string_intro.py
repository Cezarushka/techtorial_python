
str= "hello"
str1= "hello"
str2="heLlo"
# == sign is case sensitive, so if cases of 2 str is different it will return False

print(str==str1)

print(str==str2) # since the case is different(lower case and upper case) the result will be false


#we can reassign and change the string values as we are able to do with other
#data types

str2="hello"
print(str2) #will be regular hello, without upper caase because we 
#reassigned the value in this line


#since we reassigned and changed the value of str2, 
#equal comparisson(==) str2 and str1 will give the result as True

print(str2==str)






#concatinating the strings

#concatination is adding more string to the existing string value.

#EX

str2=str2+ " world"
print(str2)

# we can use concatination even when we are creating the string variable 1st time


str3= "hello" + " world"
print(str3)


str4=str+str1
print(str4) # hellohello














































