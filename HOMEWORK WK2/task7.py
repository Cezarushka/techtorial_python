

print("Enter random word")
word=input()

print("enter number of letters")
num=int(input())

print("enter a letter you want to learn")
letter=input()

lenght_of_word= len(word)

if lenght_of_word==num:
    print("True")
else:
    print("False")

print(word.find(letter))













