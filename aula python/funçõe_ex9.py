#Crie uma funçaõ que receba uma lista de strings e retorna uma nova lista
#contendo apenas strings que tem mais de X caracteres

def x(lista, letras):
    array = []
    for palavra in lista:
        y = len(palavra)
        if y > letras:
            array.append(palavra)
    return array

lista = input("Digite uma lista de palavras: ").split(", ")
letras = int(input("Digite o número mínimo de letras em cada palavra: "))

print(x(lista, letras))