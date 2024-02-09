#Escreva um programa que mostre todos os números entre 5 e 100 que 
#são divisíveis por 7 mas não são múltiplos de 5

for numero in range(5,100):
    if numero % 7 == 0 and numero % 5 != 0:
        print(numero)