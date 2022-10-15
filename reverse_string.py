#REVERSE THE WORD ENTERED BY THE USER
#MY SOLUTION
word = str(input("Write something: "))
list_word = []
for i in word:
    list_word.append(i)

index = len(list_word)-1
inverse = []

for i in range(len(list_word)):
    inverse.append(list_word[index])
    index -= 1

for i in inverse:
    print(i, end="")

#ANSWER:
def reverseString(string):
    newString = ""
    i = len(string)-1
    while i >= 0:
        newString += string[i]
        i -= 1
    return newString
print("")
palavra = str(input("Write something: "))
x = reverseString(palavra)
print(x)