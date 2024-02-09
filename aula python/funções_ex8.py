#Crie uma função que receba uma lista de numeros e retorne TRUE se todos os valores da lista
#estiverem em um determinado intervalo definido, e FALSE caso contrario


def brahma(lista, inicio, fim):
    for num in lista:
        if num > inicio or num < fim:
            return True
    return False

numero = list(map(int, input("Digite uma série de números: ").split(", ")))
print(brahma(numero, 15, 45))