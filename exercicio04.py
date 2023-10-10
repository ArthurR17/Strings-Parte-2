palavra = input("Digite uma palavra: ") # Pede para o usuário digitar uma palavra

for i in range(len(palavra)):
    for j in range(i + 1, len(palavra)):
        print(palavra[i:j])