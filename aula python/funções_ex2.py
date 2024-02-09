#Desenvolva  um programa que receba uma frase(string) e retorne o número de ocorrências de um
#determinado caractére na frase usando uma função


def carac(frase, letter):
    contador = 0
    for letra in frase:
        if letra == letter:
            contador += 1
    return contador

texto = input("Digite uma frase: ")
ltr = input("Digite uma letra presente na frase: ")
print(carac(texto,ltr))
