#Escreva um programa que leia o arquivo poema.txt e retorne na tela
#apenas as palavras com mais de 6 caracteres

arquivo = open("poema.txt" , "r", encoding="UTF-8")

for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        if len(palavra) > 6:
            print(palavra)
arquivo.close()