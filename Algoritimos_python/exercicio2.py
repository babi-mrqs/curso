#Desenvlva uma calculadora que peça ao usuário 2 valores e em seguida pergunte qual operação deve ser feita(+,-,/,*)
#e printe o resultado na tela

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que você deseja realizar (+, - , *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Operação inválida.")