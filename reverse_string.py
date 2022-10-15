#INVERTA A PALAVRA INSERIDA PELO USUÁRIO
#MEU DESENVOLVIMENTO
l = str(input('Informe uma palavra: '))
lista = []
for i in l:
    lista.append(i)

index = len(lista)-1
inverso = []

for i in range(len(lista)):
    inverso.append(lista[index])
    index -= 1

for i in inverso:
    print(i, end="")

#RESPOSTA DO PROBLEMA:
def reverseString(string):
    newString = ""
    i = len(string)-1
    while i >= 0:
        newString += string[i]
        i -= 1
    return newString

palavra = str(input("Digite algo: "))
reverseString(palavra)