def swapi(x):
 k = ''
 for i in x:
    if i.islower():
        k += i.upper()
    else:
        k += i.lower()
 return(k)

word = input("Enter a word:")
ret = swapi(word)
print(ret)
