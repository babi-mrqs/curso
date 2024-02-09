#Faça um programa em python que solicite a data de nascimento do usuário (dd/mm/aaaa)
#e imprima a data com o nome do mês por extenso

entrada = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
data = entrada.split("/")
meses = [0,'janeiro','fevereiro', 'março','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
print(f"{data[0]} de {meses[(int(entrada.split('/')[1])-1)]} de {data[2]}.")


