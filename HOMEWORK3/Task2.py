
print("Enter minimum number")
minimum_number=int(input())

print("Enter Maximum Number")
maximum_number=int(input())

sum=0
text=""
for number in range(minimum_number,maximum_number+1):
    if number%3==0 and number%11==0:
        text=text+str(number) + "+"
        sum+=number

print("0,99 ->",text.removesuffix("+"),"=" , sum)


















