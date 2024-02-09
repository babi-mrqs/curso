#Escreva um programa que peça ao usuário um número e verifique se esse número é impar ou par

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(num, "é par.")
else:
    print(num, "é impar.")

