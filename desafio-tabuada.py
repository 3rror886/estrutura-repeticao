#"Parado ai visitante"

tabuada = int(input("digite a tabuada que você deseja: "))
contador = 0
extensão = int(input("digite até a onde você deseja que sua tabuada siga: "))

sim = True
nao = False

if tabuada < 0:
    print("errado numeros negativos não são permitidos")
elif contador < 0:
    print("errado numeros negativos não são permitidos")
else:
    while contador <= extensão:
        print(tabuada, "x", contador, "=", contador * tabuada)
        contador += 1
    


