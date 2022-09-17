
number_of_student=36
str="total number of student is",number_of_student
print(str)

number_of_student=36
str="total number of student is {}"
print(str.format(number_of_student))


number_of_teacher=12

#create a stringthat shows number of teachers and number of student

s="total number of teachers is {} and the total number of student is {}"
print(s.format(number_of_teacher,number_of_student))

#Using index numbers for formatting the string, it HAS TO START FROM 0

s="total number of teachers is {1} and the total number of student is {0}"
print(s.format(number_of_student,number_of_teacher))




s=f"total num of teachers is{number_of_teacher}"

print(s)
























