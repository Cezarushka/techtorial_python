a= 5
print(a)

a = a+10
print(a)
# a will be 15 because a=5+10=15

b= 4
b=b*a
print(b)

# b will be 60 because a=15 * b(4) so 15*4=60

# if there is multipplication or dividing in any equation,
# multiplication and division will be first, then minus and plus.


a = a-b+b/4+a*7-7

print(a)

#the value of a will be 
# a=15, b=60, so 15-60+60/4+15*7= 15-60+15+105-7= -45+15+105-7= 68.0
# every time there is a division, the end number will be a decimal( in this case 68.0)
# if there is an equation with 2 operations that have priority, in this case / and *, 
#the computer will calculate from left to right as priority to others, in this case
# /division has priority over * multiplication


 








