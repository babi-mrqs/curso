#Desenvolva um programa que receba uma arra de números inteiros e verifique se um número específico está 
#dentro do array, solicite o número ao usuário.

array = [ 20,25,23,21,36,96,45]
num = int(input("Digite um número: "))

if num in array:
    print("O número", num, "está no array.")
else:
    print("O número", num, "não está no array.")