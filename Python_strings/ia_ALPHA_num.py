
#isalpha() method
#it only retunrs True when all charachters are letters

s="this is text"
print(s.isalpha())  #false because there are spaces

#s=s.replace(" ","")
print(s.isalpha())#true because we used replace method in removing spaces from the string

print(s.replace("","-").isalpha()) #false because "-" is not a letter

print(type(s.isalpha()))

#ISNUMERIC method
#all ch need to be numbers

s1="777-777-7777"
print(s1.isnumeric()) #false because "-" in not a number

print(s1.replace("-","").isnumeric())


s1="7777b4eh3"
print(s1.isnumeric()) #false beacuse contains letters



#ISALNUM() method
#if all ch are numbers and letters

print(s1.isalnum()) #true because it consits num and letters

s2="string"
s3="77777"
print(s2.isalnum()) #true, it contains one of them
print(s3.isalnum()) #true, it contains one of them
s4 = "478eiuhjr847iu"
s5 ="ksjadl45-"
print(s2.isalnum())   # True
print(s2.isnumeric()) # False
print(s2.isalpha())   # True
################################
print(s3.isalnum())   # True
print(s3.isnumeric()) #True
print(s3.isalpha())   #False
################################
print(s4.isalnum())   # True
print(s4.isnumeric()) # False
print(s4.isalpha())   # False
################################
print(s5.isalnum())   # False
print(s5.isnumeric()) # False
print(s5.isalpha())   # False






















