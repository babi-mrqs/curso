#desenvolva um programa que peça ao usuário sua idade e exiba umma mensagem indicando se ele é uma criança (0 a 12 anos)
#um adolescente(13 a 17 anos),a dulto (18 a 59 anos), ou idoso (+ 60 anos)
idade = int(input("digite a idade: "))

if(idade <= 12):
    print("Você é criança!")
elif(idade <= 17):
    print("Você é adolescente!")
elif(idade <= 59):
    print("Você é adulto!")
else:
    print("Você é idoso!")