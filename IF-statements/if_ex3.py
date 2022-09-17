
#as user to give 2 integer number, find the sum of these 2 integer num
#if sum of the 2 integer num is smaller than 10
#prin "sum of these 2 num is 10"
#if sum of these 2 num is between 10 and 19 including
#print "sum of these 2 num is 20"
#all other conditions print" prin the actual sum of these 2 num


print("Please insert two integer numbers")
num1=int(input())
num2=int(input())
sum=num1+num2
if sum<10:
    print("sum is 10")
elif sum>=10 and sum<=19:
    print("sum is 20")
else :
    print(f"sum of these num is{sum})"

