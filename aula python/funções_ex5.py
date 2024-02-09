#Crie uma função que receba uma lista de números e retorne a média dos valores

def mediaa(lista):
    x = len(lista)
    y = sum(lista)
    media = y / x
    return media 

x = list(map(int, input("Digite os números: ").split(", ")))

print("A média é " , mediaa(x))
