#Escreva um código que use uma função que certifica se uma palavra digitada pelo usuário é um palíndromo 

# word = input(("Escreva uma palavra para verificar se ela é um palíndromo: "))
# if str(word) == "".join(reversed(word)) :
#     print("Palindrome")
# else:
#     print("Not Palindrome")

def palin(palavra):
    palavra = palavra.lower()
    for letra in range(len(palavra)//2):
        if palavra[letra] != palavra[-letra-1]:
            return False
    return True

word = input("Escreva uma palavra para verificar se ela é um palíndromo: ")
print(palin(word))