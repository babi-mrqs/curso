#Escreva um código que tenha uma função que recebe uma lista de numeros e retorna a soma de todos os números

def somar(x):
    soma = 0
    for num in x:
        soma += num
    return soma

numeros  = list(map(int, input("Digite os números: ").split(", "))) 
resultado = somar(numeros)
print(resultado)


