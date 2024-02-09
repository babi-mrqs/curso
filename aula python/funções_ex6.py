#Crie uma função que receba um lista de números positivos e retorne True caso todos os valores da
#lista forem positivos e False caso contrario

def valor(lista):
    for num in lista:
        if num < 0:
            return False
    return True
    
x = list(map(int, input("Digite os números: ").split(", ")))
print(valor(x))