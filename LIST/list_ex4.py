
#create  program that will ask user 10 full anmes
#after you get the names, create email version of given 10 names and store it in a list and print




full_names=[]
emails=[]
for i in range(10):
    print("enter a full name")
    f_name=input()
    full_names.append(f_name)
    f_name=f_name.replace(" ","").lower()+"gmail.com"
    emails.append(f_name)

print(full_names)
print(emails)







