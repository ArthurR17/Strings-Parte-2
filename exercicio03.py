texto = input("Digite sua string: ")  # pede ao usuário para digitar uma string

palavras = texto.split()  # divide a string em uma lista de palavras

frequencias = {}  # cria um dicionário vazio

for palavra in palavras:  # para cada palavra na lista de palavras
    if palavra in frequencias:  # se a palavra já está no dicionário
        frequencias[palavra] += 1  # adiciona 1 à sua frequência
    else:
        frequencias[palavra] = 1  # senão, adiciona a palavra ao dicionário

print(frequencias)  # imprime o dicionário de frequências