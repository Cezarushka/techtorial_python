

#print numbers from 1-10 inclusive
num=1
while num<=10:
    print(num) # it wont stop. i have to update the value of num so the cond will be false eventually.
    num=num+1



#print even num that are smaller than  <=10
num=2
while num<=10:
    print(num)
    num=num+2
print(f"value or the variable num is {num}")



num=1
while num<=10:
    if num%2==0:
        print(num)
    num +=1

#from 1-20 print every odd number in following fromat
#this is an odd number {value of the number}

#print every even number
#thi ia an even number {value of number}
num=1
while num<=20:
    #in the while loop i have to decide num is currently even or odd
    if num %2==1:
       print(f"odd number {num}")
    else:
        print(f"even number {num}")
    num+=1














