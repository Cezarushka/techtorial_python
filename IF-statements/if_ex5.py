#ask user to enter date in format of mm/dd/yyyy
#convert given date like following ex:
#03/-6-2017 -->march 6, 2017

#07/10/2022   ->july, 10, 2022

print("please enter date in format mm/dd/yyyy")
date=input()
#fisrt 2 ch og the given date will give you the month
month=date[0:2]
day=date[3:5]
year=date[-4:]


if month=="01":
    print(f"Jan {day},{year}")
elif month=="02":
    print(f"Feb {day},{year}")
elif month=="03":
    print(f"March {day},{year}")    
elif month=="04":
    print(f"Apr {day},{year}")    
elif month=="05":
    print(f"May {day},{year}")    
elif month=="06":
    print(f"Jun {day},{year}")    
elif month=="07":
    print(f"Jul {day},{year}")    
elif month=="08":
    print(f"Aug {day},{year}")    
elif month=="09":
    print(f"Sept {day},{year}")    
elif month=="10":
    print(f"Oct {day},{year}")    
elif month=="11":
    print(f"Nov {day},{year}")    
elif month=="12":
    print(f"Dec {day},{year}")    








