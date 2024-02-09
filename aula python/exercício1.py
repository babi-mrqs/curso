#Escreva um programa que peça ao usuário dois números indicando qual dos números é maior ou menor. Tambem indicar caso os números forem iguais

A = int(input("digite um número de 0 a 10: "))
B = int(input("digite um segundo núemro de 0 a 10: "))

if(A > B):
    print("O ", A ," número é maior")
elif(A==B):
    print("Os núemros são iguais")
else:
    print("O ", B ," é maior")