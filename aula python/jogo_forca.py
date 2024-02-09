#Crie uma função que implemente o jogo da forca
#A função deve receber a plavra a ser descoberta pelo jogador e o número de tentativas. 
#O programa deve permitir que o usuário adivinhe as letras até descobrir a palavra completa
#Ou receber o número de tentativas
#Usa while, break, if, array, in, for


def jogo_forca(palavra, max_tentativas):
    certas = set()
    erradas = set()
    tentativas = 0
    while True:
        letra = input("Digite uma letra: ").lower()
        if letra in palavra:
            certas.add(letra)
            if certas == set(palavra):
                print("Parabéns, Você ganhou")
            break
        else:
            erradas.add(letra)
            tentativas += 1
            print("Você digitou uma letra errada, ainda restam ", max_tentativas - tentativas , "tentativas.")
            if tentativas >= max_tentativas:
                print("Você atingiu o número máximo de tentativas!")
                break
        posicoes_certas = []
        for indice, letter in enumerate(palavra):
            if letter in certas:
                posicoes_certas.append(indice)
        resultado = ""
        for indice, letter in enumerate(palavra):
            if letter in certas:
                resultado += letter
            else:
                resultado += "_"




# def jogo_forca(palavra,max_tentativas):
#     palavra = palavra.lower()
#     letras_certas = set()
#     letras_erradas = set()
#     tentativas = 0
#     while True:
#         letra = input("Digite uma letra: ").lower()
#         if letra in palavra:
#             letras_certas.add(letra)
#             if letras_certas == set(palavra):
#                 print("Parabéns, você acertou!")
#                 break
#         else:
#             letras_erradas.add(letra)
#             tentativas += 1
#             if tentativas >= max_tentativas:
#                 print("Você excedeu o número máximo de tentativas")
#                 break
#             posicoes_corretas = []

#     for i, I in enumerate(palavra):
#         if I in letras_certas:
#             posicoes_corretas.append(i)

#     resultado = ''
#     for i, I in enumerate(palavra):
#         if i in posicoes_corretas:
#             resultado += I
#         else:
#             resultado += '_'  
#             print(f"Palavra: {resultado}")
#             print(f"Letras certas: {letras_certas}")
#             print(f"Letras erradas: {letras_erradas}")

# palavra1 = 'abacate'
# max_tentativas1 = 9
# print(jogo_forca(palavra1,max_tentativas1))


