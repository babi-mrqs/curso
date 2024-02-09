cidades = input("DIgite os nome de cidade separando-os por espaço: ").split(",")

print(cidades)


remover = input("Qual cidade será removida? ")

cidades.remove(remover)

print(cidades)