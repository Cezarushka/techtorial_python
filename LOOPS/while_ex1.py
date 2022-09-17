
#ask user to give u a string 
#from that string print index number of all the E's


print("enter text")
str=input()
#we can access string elements  using their indexes
index=0

#index num will alsways be smaller than the LENGHT of the string

lenghts_of_str= len(str)

while index<lenghts_of_str:
    if str [index] == "e":
        print(f"index num of e is{index}")
    index +=1



















