
#prefix-will remove from the beginning of the string
#suffix-will remove from the end of the string

s="hello  python"
#if you want to remove python from this string, use remove suffix method

print(s.removesuffix("python"))


print(s.removeprefix("hello"))


#from the given website, print only the domain of website
web_site=input()
domain_name=web_site.removeprefix("www.").removesuffix(".com")
print(domain_name)


str="hello world"
print(str.removeprefix("el"))

str2="encapsulation is good for data hiding"
print(str2.removesuffix("ing"))

print("Result of the suffix",str2.removesuffix("gni"))
print("Result of strip",str2.strip("gni"))
#  "Encapsulation is good for data hiding"
#  "Encapsulation is good for data hid"
#  "Encapsulation is good for data hidi"

















