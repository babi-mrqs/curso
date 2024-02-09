#Crie um programa que receba um array de número via input, em seguida, retorne a média dos números inseridos

num = list(map(float, input("Digite os números: ").split(", ")))
#soma = 0

#for numero in num:
    #soma = soma + numero
    #soma += numero

x = len(num)
y = sum(num)

media = y / x
print(media)
