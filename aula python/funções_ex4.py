#Crie uma função que receba uma lista de números e retorne o maior valor encontrado na lista


# def maior(numero):
#     num = max(numero)
#     return num
    
def enc_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

x = list(map(int, input("Digite os números: ").split(", ")))

print(enc_maior(x))