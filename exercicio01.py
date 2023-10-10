palavra = input("Digite uma palavra: ") # Pede para o usuário digitar uma palavra
palavra2 = input("Digite a mesma palavra que digitou anteriormente porém ao contrário: ") # Pede para o usuário digitar a mesma palavra que digitou anteriormente porém ao contrário

palavra = palavra.lower() # Transforma a palavra em minúscula
palavra2 = palavra2.lower() # Transforma a segunda palavra em minúscula


if sorted(palavra) == sorted(palavra2): # Se a palavra digitada for igual a palavra digitada ao contrário
    print("As palavras são anagramas!") # Imprime que as palavras são anagramas
else:
    print("As palavras não são anagramas!") # Senão imprime que as palavras não são anagramas