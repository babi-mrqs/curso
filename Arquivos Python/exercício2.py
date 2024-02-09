#Crie um programa que leia as informações gravadas no arquivo dados.txt e exiba
#na tela o nome, idade e cidade do usuário

arquivo = open("Dados.txt" , "r")
informações = arquivo.read().split(", ")
arquivo.close()
nome = informações[0]
idade = informações[1]
cidade = informações[2]
print(nome)
print(idade)
print(cidade)