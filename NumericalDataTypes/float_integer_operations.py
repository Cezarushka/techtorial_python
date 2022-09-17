#every math operation between float and integer data type
#will result in float data type


floatNum=3.0
intNum=5

print("type of floatNum is", type(floatNum))
print("type of intNum is", type(intNum))

addition = floatNum + intNum
print("addition of float and int is", type(addition))

subtraction=intNum-floatNum
print("subtraction between int and float", (subtraction))

mutliplication=floatNum* intNum
print("multiplication between int data type and float is", type(mutliplication))

division= intNum/ floatNum
print("the division between float and int data type is", type(division))

remainder=floatNum%intNum
print("the remainder between float and int data is", type(remainder))

remainder2= intNum%floatNum
print("the remainder between float and int", type(remainder2))

int_division= floatNum// intNum
print("the integer symbol division result between float and integer is", type(int_division))

square_of_float= floatNum* floatNum
print(type(square_of_float))