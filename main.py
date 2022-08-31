receber = input("Digite algo aqui:")

with open("arquivo.txt", "a") as arquivo:
    arquivo.write(f'{receber}\n')
