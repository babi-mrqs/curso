#Embaralhador de palavras:
#Desenvolva uma função que receba uma palavra como parâmetro e retorne a mesma palavra com suas
#letras embaralhadas de forma aleatória

from random import shuffle

def embaralhar_palavras(palavra):
    a = list(palavra)
    shuffle(a)
    x = "".join(a)
    return x

entrada = input("Digite uma palavra: ")

print(embaralhar_palavras(entrada))