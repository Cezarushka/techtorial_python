#create a python program to give most efficient exchange possible
#using only coins

#quarter
#dime
#nickel
#penny


#$2.34 of exchange

#9 QUARTERS
#30dimes
#1 nickel
#4 pennies

Dollar_amount =2.36

quarter_value= .25
dime_value =.10
nickel_value =.05
penny_value = 0.01

count_of_q= Dollar_amount // quarter_value
print(count_of_q)

remaining_exchange_after_q =Dollar_amount% quarter_value
count_of_d= remaining_exchange_after_q//dime_value
remaining_exchange_after_d= remaining_exchange_after_q//nickel_value
count_of_nickel=remaining_exchange_after_d