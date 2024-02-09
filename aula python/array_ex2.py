#crie um programa que leia uma lista de nomes como entrada do usuário  e 
#conte quantos elementos na lista começam com a letra A

nomes = input("Digite uma lista de nomes, separado por ,: ").split(",")
contador = 0
for y in nomes:
    if y.startswith("A"):
        #contador += 1
        contador = contador + 1

print(nomes)
print(contador)