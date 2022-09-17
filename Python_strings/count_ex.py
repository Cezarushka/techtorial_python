#ask user to give 2 str values
#if 1st string contains 2nd string return true, if not, return false
print("enter text one")
s1=input()
print("enter text two")
s2=input()

#if the 1st string doesnt contain the 2nd string, the count of seconf string in the forst one should be0


count_ofsecond=s1.count(s2)

print(count_ofsecond)

is_contain=bool(count_ofsecond)

print(is_contain)



