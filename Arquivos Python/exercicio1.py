#Crie um programa que solicite ao usuário seu nome, idade e cidade, Em seguida
#grave essas informações em um arquivo chamado dados.txt, separando estas informações com uma vírgula

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite o nome da sua cidade: ")
#print(nome,idade,cidade)
# x = nome +", " + idade + " e "+cidade + "."
arquivo = open("Dados.txt","w")
arquivo.write(f"{nome}, {idade}, {cidade}.")
arquivo.close()