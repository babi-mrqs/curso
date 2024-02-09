#Faça um programa que encontre o maior valor dentro da lista [1,2,4,3,20,12,13,31]

lista = [1,2,4,3,20,12,13,31]

num = 0
for numero in lista:
    if numero > num:
        num = numero
print("O maior número é " , num)