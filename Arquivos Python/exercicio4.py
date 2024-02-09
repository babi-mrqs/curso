#Escreva um programa que conte o número de linhas presentes no arquivo poema.txt
#e exiba na tela este número

arquivo = open("poema.txt" , "r", encoding="UTF-8")
contador = 0
for linha in arquivo:
    contador += 1
arquivo.close()
print(contador)