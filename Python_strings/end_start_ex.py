

#ask user to give 2 string value and print true is 2nd string starts with last 2 charchters of the first string
#OR print true if the first string starts with first 2 characters of 2nd string


from webbrowser import Chrome


print("Enter first string")
s1 = input()

print("Enter second string")
s2 = input()

last_two_ch_s1=s1[-2:]

is_second_start=s2.startswith(last_two_ch_s1)
fisrt_two_ch_s2=s1[:2]

is_first_start=s1.startswith(fisrt_two_ch_s2)

print(is_second_start or is_first_start)













