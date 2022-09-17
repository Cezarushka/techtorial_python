#user want to deposit money in the bank account
#he already has $200 in his account
#he has 3 different paycheks (400,600,350)
#after he deposit all money in account he bouth phone for 599 and headphone for 299
#create a program to calculate his final money in the account
#use input funtion to get all the values




bank_acct=200

print("please enter 1st paycheck amount")

fisrt_deposit= int(input())
bank_acct+=fisrt_deposit

print("please enter 2nd check amount")

second_deposit=int(input())

bank_acct+=second_deposit

print("please enter 3rd paycheck amount")
third_deposit=int(input())

bank_acct+=third_deposit

print("please enter dollar amount of phone you want tobuy")
phone=int(input())
bank_acct-=phone

print("please enter dollar amount for headphones")
head_phones=int(input())

bank_acct-=head_phones

print("final money in the account is",bank_acct)













