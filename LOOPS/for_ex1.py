

#ask user a given string and duplicate each letter in the given string
# input abc, output shoul be aabbcc
#input is def, output is ddeeff

print("enter text")
str=input()

duplicated=""
for l in str:
    duplicated+=l
    duplicated+=l
print(duplicated)





















