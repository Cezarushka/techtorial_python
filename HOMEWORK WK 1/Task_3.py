#give the right amount in quartes,dimes, nickels and pennies
#$2.36 of exchange
dollar=5.22
dollar_amount=dollar*100

quarter_value=25
dime_value=10
nickel_value=5
penny_value=1



quarter_amount=dollar_amount//quarter_value



remaining_exchange_after_quarters=dollar_amount%quarter_value


amount_of_dimes=remaining_exchange_after_quarters//dime_value


remaining_exchange_after_dimes=remaining_exchange_after_quarters%dime_value
amount_of_nickels=remaining_exchange_after_dimes//nickel_value


remaining_exchange_after_nickels=remaining_exchange_after_dimes%nickel_value
amount_of_pennies=remaining_exchange_after_nickels//penny_value
print("Total change is ", (int(quarter_amount)), "quarters",(int(amount_of_dimes)), "dimes", (int(amount_of_nickels)), "nickels", (int(amount_of_pennies)), "pennies")