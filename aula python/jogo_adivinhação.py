#Jogo da adivinhação:
#Escreva um programa que gere um número aleatório de 1 a 100, solicitando ao usuário que adivinhe qual 
#é o número gerado. O programa deve continuar solicitando até o usuário acertar o número.
#

import random
num = random.randint(1,100)

while True:
    entrada = int(input("Adivinhe um número de 1 a 100: "))
    if entrada == num:
        print("Parabéns!!! Você acertou.")
        break
    elif entrada > num:
        print("O número é menor que" , entrada)
    elif entrada < num:
        print("O número é maior que" , entrada)