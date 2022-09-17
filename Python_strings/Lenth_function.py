

#len() function allows us to learn how many charachters are used to creat a string
#len function counts spaces as well


str= "Techtorial"
str1=" Techtorial "
print(len(str))
print(len(str1))


#len function will return integer value so we can assign integer variables using len function

len_of_str= len(str)
print(len(str))
print(type(len_of_str))

#create a program to print true if the len of str is even number

#even number can be divided by 2


is_len_even = len_of_str % 2 == 0
print(is_len_even)



























