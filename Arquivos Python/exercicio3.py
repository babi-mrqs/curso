#Escreva um programa que leia o conteúdo do arquivo "poema.txt" linha por linha
#e mostre o mesmo


arquivo = open("poema.txt" , "r", encoding="UTF-8")
for linha in arquivo:
    print(linha)
arquivo.close()