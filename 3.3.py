#d)List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

word=input("Enter a word:")
list=[ord(x) for x in word]
print(list)