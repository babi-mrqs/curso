#Escreva um programa que realize a contagem de todas as palavras dentro do arquivo poema.txt

arquivo = open("poema.txt" , "r", encoding="UTF-8")
contador = 0
# info = arquivo.read().split(" ")
# for palavra in info:
#     contador += 1

# for linha in arquivo:
#     palavra =  linha.split(" ")
#     contador += len(palavra)
    
info = arquivo.read()
palavras = info.split()
contador = len(palavras)
arquivo.close()
print(contador)