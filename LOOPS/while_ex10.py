

#ask user to enter as tring
#if the given string contains any dublicated letter
#print"str has dub
#otherwise, print string consist of unique letter

print("enter a string")
str=input()
is_unique=True
index=0
while index<len(str):
    if str.count(str[index])>1:
        is_unique=False
        break
    index+=1
if is_unique:
    print("string is unique")
else:
    print("string is dubl")




















