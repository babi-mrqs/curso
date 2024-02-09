#Crie um programa que receba um array de números e retorna um novo array com os números elevados ao quadrado

num = list(map(int, input("Digite os números: ").split(", ")))

abc = []

for numero in num:
    abc.append(numero**2)

print(abc)