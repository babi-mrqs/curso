# Desenvolva uma Calculadora de IMC, o programa deve pedir o peso e a altura do usuário
# Cacular o IMC e retornar ao usuário o IMC e a categoria em que se encontra

#Menor que 18,5 - Abaixo do peso
#Entre 18,5 e 24,9 - Peso normal
#Entre 25 e 29,9 - Sobrepeso
#Acima de 30 - Obesidade

def imc(peso,altura):
    abx = "Está abaico do peso."
    nrm = "Seu peso é normal."
    sbr = "Você está com sobrepeso."
    obs = "Você está obeso"
    x = peso/(altura*altura)
    if x < 18.5:
        return x, abx
    elif x >= 18.5 or x <= 24.9:
        return x, nrm
    elif x >= 25 or x <= 29.9:
        return x, sbr
    else:
        return x, obs
    
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
print("Seu imc é", imc(peso, altura))