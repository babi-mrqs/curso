#Crie um programa que receba um array de um número e retorna a soma dos números impares


num = list(map(int, input("Digite os números: ").split(", ")))
soma = 0
for numero in num:
   if (numero % 2) != 0:
      soma += numero

print(soma)
 
 