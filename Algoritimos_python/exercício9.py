#desenvolva uma função que receba o valor do produto e a porcentagem de desconto, e retorne o valor com desconto aplicado


def desc(valor,porcentagem):
    desconto = (porcentagem/100) * valor
    resultado = valor - desconto
    return resultado

print(desc(1500,10))