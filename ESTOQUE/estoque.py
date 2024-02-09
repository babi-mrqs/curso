#Desenvolva um sistema de estoque que utiliza um arquivo de texto como banco de dados.
#Devemos considerar que cada item do estoque possui Nome, quantidade e um preço.
#O sistema deve ter no mínimo três funções

# 1 função para listar os itens;
# 1 função para buscar um item específico;
# 1 função para adicionar um novo item.
# Ao iniciar, deverá abrir um menu de opções, onde o sistema deve pedir ao usuário se ele
#deseja listar, buscar ou adicionar um item
# O sistema só deve fechar se o usuário escolher a opção "Sair" no menu de opções

# estoque1 = open("estoque.txt","w")
# estoque1.close()

def listar_itens():
    arquivo = open("estoque.txt","r")
    for linha in arquivo:
        informacoes = linha.strip().split(',')
        print(f"nome: {informacoes[0]}, quantidade: {informacoes[1]}, preço: {informacoes[2]}")
    arquivo.close()

def buscar_item(nome):
    arquivo1 = open("estoque.txt","r")
    for linha in arquivo1:
        dados = linha.strip().split(',')
        if dados[0] == nome:
            return {'nome:': dados[0], 'quantidade': int(dados[1]), 'preço' : float(dados[2])}
        else:
             return "Item não encontrado"
    arquivo1.close()

def adicionar_item(a,b,c):
    arquivo = open("estoque.txt","a")
    arquivo.write(f'{a},{b},{c}.\n')
    arquivo.close()
    return "O item foi adicionado com sucesso"


while True:
    print("1 - Listar os itens\n2- Buscar um item\n3- Adicionar um item\n4- Sair")
    opcoes = input("Escolha uma das opções acima: ")
    if opcoes == "1":
        print(listar_itens())
    elif opcoes == "2":
        item = input("Digite o nome do item que você quer buscar: ")
        print(buscar_item(item))
    elif opcoes == "3":
        nome = input("Digite o nome do produto que você quer adicionar: ")
        quantidade = input("Digite a quantidade do produto: ")
        valor = input("Digite o valor do produto: ")
        print(adicionar_item(nome, quantidade, valor))
    elif opcoes == "4":
        break
    else:
        print("Você digitou uma opção inválida, tente novamente.")
