#Escreva um programa que peça ao usuário três notas e calcule a média. Em seguida, 
#o programa deve exibir a média calculada e uma mensagem indicando se o aluno foi 
#aprovado (média maior ou igua a 7), reprovado (média menor que 5) ou se está de 
#recuperação (média entre 5 e 6.9).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma = (nota1 + nota2 + nota3 + nota4)

média = soma / 4

if(média >= 7):
    print("Aprovado")
elif(média < 5):
    print("Reprovado")
else:
    print("De recuperação")