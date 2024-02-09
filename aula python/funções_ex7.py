#Crie uma função que receba uma palavra e retorne o número de vogais presente na palavra

# def vog(palavra):
#     cont = 0    
#     for letra in palavra:
#         if (letra == "a" or letra == "A"
#         or letra == "e" or letra == "E"
#         or letra == "i" or letra == "I"
#         or letra == "o" or letra == "O"
#         or letra == "u" or letra == "U"):
#             cont += 1
#     return cont

def vog(lista):
    vogais = "aeiouAEIOU"
    contvog = []
    for palavra in lista:
        contagem = 0 
        for letra in palavra:
             if letra in vogais:
                contagem += 1
        contvog.append(contagem)
    return contvog

abc = input("Digite as palavras: ").split(", ")
print("O número de vogais são " , vog(abc))   