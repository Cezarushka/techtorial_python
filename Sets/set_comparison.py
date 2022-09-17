
s1={1,7,9,3}

s2={2,7,9,5}

print(s1.difference(s2))

#difference method will show ellements that are present in one line but not present in other

print(s2.difference(s1))
print(type(s2.difference(s1)))


#Intersection

s1={1,7,9,3}

s2={2,7,9,5}

print(s1.intersection(s2)) #it will print the common ellements from both sets


#issubset()

s1={1,2,3,4,5}

s2={2,3,4}

print(s1.issubset(s2)) #cheks if given set is present in the other IT WILL PRINT  False
print(s2.issubset(s1)) #will print True

#Superset, if the set has all the elements of other set

s1={1,2,3,4,5}

s2={2,3,4}
print(s1.issuperset(s2))

#update method- INTERSECTION_Update

#it will remove all the elements that are not present on the other set

s1={1,2,3}

s2={2,3}
s1.intersection_update(s2)
print(s1)

#DIFFERENCE_UPDATE


s1={1,2,3}

s2={2,3}
s1.difference_update(s2)
print(s1)
s3={1,2,3}
s2.difference_update(s3)
print(s2) #empty set 















