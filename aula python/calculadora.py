numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um segundo número: "))
operação = input("Digite a operaçãp que deseja realizar (+,-,*,/): ")

soma = (numero1 + numero2)
sub = (numero1 - numero2)
div = (numero1 / numero2)
mult = (numero1 * numero2)

if(operação == "+"):
    print(soma)
elif(operação == "-"):
    print(sub)
elif(operação == "/"):
    print(div)
elif(operação == "*"):
    print(mult)
else:
    print("Você digitou uma operação inválida, tente novamente.")
