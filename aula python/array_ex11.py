#Faça um programa que receba um número inteiro e verifique se ele é primo ou não


num =  int(input("Digite um número: "))

cont = 0

for x in range(2,num):
    if (num % x) == 0:
        print(num , " não é primo")
        cont += 1

if(cont < 1):
    print(num, " é primo")