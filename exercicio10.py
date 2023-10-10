cofre1 = "Zeus"
cofre2 = "Poseidon"
cofre3 = "Hades"
cofre4 = "Athena"
cofre5 = "Demeter"
cofre6 = "Hermes"
cofre7 = "Ares"
cofre8 = "Afrodite"
cofre9 = "Artemis"
cofre10 = "Cronos"

senha = input("Digite a senha do cofre: ")
deslocamento = int(input("Por favor, digite o deslocamento: "))
textoCifrado = ""

for char in senha:
    if char.isalpha():
        codigo = ord(char)
        codigo += deslocamento
        if char.isupper():
            if codigo > ord('Z'):
                codigo -= 26
            elif codigo < ord('A'):
                codigo += 26
        else:
            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26
        textoCifrado += chr(codigo)
    else:
        textoCifrado += char


print("Texto cifrado: ", textoCifrado)
