#Crie um programa que recebe um array de números e retorna o maior e menor número


num = list(map(int, input("Digite os números: ").split(", ")))

# x = min(num)
# y = max(num)

# print(x)
# print(y)

maior = num[0]
menor = num[0]

for numero in num:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print(num)
print(maior)
print(menor)
