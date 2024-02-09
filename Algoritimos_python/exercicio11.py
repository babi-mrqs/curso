#Crie uma função que receba uma string e retorne o número de vogais
def vog(palavra):
    cont = 0    
    for letra in palavra:
        if (letra == "a" or letra == "A"
        or letra == "e" or letra == "E"
        or letra == "i" or letra == "I"
        or letra == "o" or letra == "O"
        or letra == "u" or letra == "U"):
            cont += 1
    return cont