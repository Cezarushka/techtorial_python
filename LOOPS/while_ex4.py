

#aask user to enter integer num and print all the divisor of given integer num
#possible divider of given number.
#start with 1 and end at the given number itself

print("enter integer num")
num= int(input())

possible_divisor=1

while possible_divisor<=num:
    #since we have possible divisor nut we are not sure if we can divide num or not
    #how can we understand if possible divisor is an actual divisor of the num
    #if number % possible divisor=0, means its an actual divisor
    if num%possible_divisor==0:
        print(f"{possible_divisor}")
    possible_divisor+=1























