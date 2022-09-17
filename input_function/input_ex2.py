#ask user to give you text
#ask user to order number of the letter and print that letter from the text

print("enter text")
text=input()

print("emter order number of letter you wante to see")
order_number=int(input())

#we have to consider that user doesnt know about index numbers
#and the number user chose will be 1 bigger than the index number

# "python"
#  012345 -->index nrs
#  123456 -->order number user will think its true

index_number=order_number-1
print(text[index_number])