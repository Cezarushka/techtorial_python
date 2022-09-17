
nums=[1,2,3,10,11,13,17,21,26]

#fromm given list, fing sum of all the even numbers
#also letf find sum of all odds separately

sum=0
sum_odd=0
for number in nums:
    if number %2==0:
       sum+=number
    else:
        sum_odd+=number
print(number)
print("sum of all given numbers is", sum) 
print("sum of all odd numbers is",sum_odd)





















