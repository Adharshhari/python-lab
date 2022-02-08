#c)Form a list of vowels selected from a given word

a=input("Enter a word:")
vowel=["A","E","I","O","U","a","e","i","o","u"]
b=[x for x in a if x in vowel ]
print(b)