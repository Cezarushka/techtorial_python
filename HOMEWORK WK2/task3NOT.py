

print("Please  enter text of 3 words")
text=input()
text=text+" "
index=0
lenght_of_text=len(text)


while index<lenght_of_text:
    if (text[index]==" "):
        print(text[index-1])
    index=index-1
    print(index)













