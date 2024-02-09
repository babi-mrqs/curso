#Crie um  programa onde o usuário insira números, separados por 
#vírgula e atribua esses números a um array, em seguida faça um print desse array

num = list(map(int, input("Digite os números: ").split(", ")))

print(num)
print(type(num[1]))

           




