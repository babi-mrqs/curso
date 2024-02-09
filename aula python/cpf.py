#Desenvolva um programa que solice a digitação de um cpf em formato xxx.xxx.xxx-xx e
#indique se é um cpf válido ou inválido através da validação dos dígitos verificadores.

entrada = input("Digite seu CPF no formato XXX.XXX.XXX-XX: ")
                
cpf = []
cpf.append(entrada)
for numero in cpf:
    soma1 = (cpf[0]*10) + (cpf[1]*9) + (cpf[2]*8) + (cpf[4]*7) + (cpf[5]*6) + (cpf[6]*5) + (cpf[8]*4) + (cpf[9]*3) + (cpf[10]*2)
    resto1 = soma1 % 11
    soma2 = (cpf[0]*11) + (cpf[1]*10) + (cpf[2]*9) + (cpf[4]*8) + (cpf[5]*7) + (cpf[6]*6) + (cpf[8]*5) + (cpf[9]*4) + (cpf[10]*3) + (cpf[12]*2)
    resto2 = soma2 % 11
    if resto1 < 2:
        if cpf[12] != "0":
            print("O CPF é inválido")
    elif resto1 >= 2:
        digito1 = 11 - resto1
        if cpf[12] != digito1:
            print("O CPF é inválido")
    elif resto2 < 2:
        if cpf[13] != "0":
            print("O CPF é inválido")
    elif resto2 >= 2:
        digito2 = 11 - resto2
        if cpf[13] != digito2:
            print("O CPF é inválido")
    else:
        print("O CPF é válido.")