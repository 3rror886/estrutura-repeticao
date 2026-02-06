#"Parado ai visitante"

while True:
    tabuada = int(input("digite a tabuada que você deseja: "))
    contador = 0
    extensão = int(input("digite até a onde você deseja que sua tabuada siga: "))

    if tabuada < 0:
        print("errado numeros negativos não são permitidos")
    elif contador < 0:
        print("errado numeros negativos não são permitidos")

    while contador <= extensão:
        print(tabuada, "x", contador, "=", contador * tabuada)
        contador += 1
    
    print("sim ou não" )
    escolha = input("selecione uma nova tabuada: ")

    if escolha == "sim":
        print("receba")
    else:
        print("nah")
        break


