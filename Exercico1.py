import math

valor_pi = math.pi
option = -1

while option != 0:
    option = -1
    volume_string = "-1"
    volume_float = 1

    while volume_string.startswith("-") or not volume_string.endswith("ml") or volume_float < 0:
        volume_string = "-1"
        volume_float = 1

        print("Digite o volume em ml  e positivo, exemplo: 25,0690ml\nCaso deseje usar π escreva \"pi\" antes de ml:")
        volume_string = str(input("Insira o valor aqui:")).lower()
        volume_string = volume_string.replace(",", ".")
        volume_string = volume_string.replace(" ", "")

        if not volume_string.endswith("ml"):
            print("Valor inválido!!Digite um valor válido!")

        try:
            if "pi" in volume_string:
                volume_string = volume_string.replace("pi", "")
                volume_float = valor_pi

            volume_float *= float(volume_string[:-2])
        except ValueError:
            print("Valor com digitos a mais!!")
        if volume_float < 0:
            print("Valor negativo invalido!!")

    escolha_tampa = ""

    while not (escolha_tampa == "com" or escolha_tampa == "sem"):
        print("Deseja com ou sem tampa ? digite com ou sem para responder.")
        escolha_tampa = str(input("Insira a resposta aqui: ")).lower()

        if not (escolha_tampa == "com" or escolha_tampa == "sem"):
            print("Resposta inválida!!")

    if escolha_tampa == "sem":
        numeroBases = 1
    else:
        numeroBases = 2

    precoBase_string = "-1"
    precoBase_float = 1

    while (not precoBase_string.startswith("r$")) or precoBase_float < 0:
        precoBase_string = "-1"
        precoBase_float = 1
        print("Digite o preço do cm² da base positivo, exmeplo: R$1,50")
        precoBase_string = str(input("Insira o valor aqui:")).lower()
        precoBase_string = precoBase_string.replace(",", ".")
        precoBase_string = precoBase_string.replace(" ", "")

        if not precoBase_string.startswith("r$"):
            print("Valor inválido!!Digite um valor válido!")
        try:
            precoBase_float = float(precoBase_string[2:])
        except ValueError:
            print("Valor com digitos a mais!!")
        if precoBase_float < 0:
            print("Valor negativo invalido!!")

    precoLado_string = "-1"
    precoLado_float = 1

    while (not precoLado_string.startswith("r$")) or precoBase_float < 0:
        precoLado_string = "-1"
        precoLado_float = 1
        print("Digite o preço do cm² da lateral positivo, exmeplo: R$1,50")
        precoLado_string = str(input("Insira o valor aqui:")).lower()
        precoLado_string = precoLado_string.replace(",", ".")
        precoLado_string = precoLado_string.replace(" ", "")

        if not precoLado_string.startswith("r$"):
            print("Valor inválido!!Digite um valor válido!")
        try:
            precoLado_float = float(precoLado_string[2:])
        except ValueError:
            print("Valor com digitos a mais!!")
        if precoLado_float < 0:
            print("Valor negativo invalido!!")

    raio = ((precoLado_float*volume_float)/(numeroBases*precoBase_float*valor_pi))**(1/3)
    altura = volume_float/(valor_pi*raio**2)

    TotalBase = numeroBases*precoBase_float*valor_pi*raio**2
    TotalLado = precoLado_float*2*valor_pi*raio*altura
    Total = TotalLado+TotalBase
    print("\n\n\tCalculos:" +
          "\nRaio:" +
          "\nRaio^3 = (Preço Lateral * Volume)/(Numero de Bases * π * Preço Base)" +
          f"\nRaio^3 = ({precoLado_string.upper()} * {volume_string.upper()})/({numeroBases} * {valor_pi:.3} * {precoBase_string.upper()}) " +
          f"\nRaio^3 = {(precoLado_float*volume_float)}/ {(valor_pi*precoBase_float)}" +
          f"\nRaio^3 = {((precoLado_float*volume_float)/(valor_pi*precoBase_float*numeroBases)):}" +
          f"\nRaio = {((precoLado_float*volume_float)/(valor_pi*precoBase_float*numeroBases)):}^(1/3)" +
          f"\nRaio = {(((precoLado_float*volume_float)/(valor_pi*precoBase_float*numeroBases))**(1/3)):.4}cm" +
          "\n\nAltura:" +
          "\nAltura = Volume/(π * Raio^2)" +
          f"\nAltura = {volume_float}/({valor_pi:.3} * {raio}^2)" +
          f"\nAltura = {volume_float}/({valor_pi:.3} * {raio**2})" +
          f"\nAltura = {volume_float}/{(valor_pi*(raio**2)):.4}" +
          f"\nAltura = {(volume_float/(valor_pi*(raio**2))):.4}cm" +
          "\n\nPreço Base:" +
          "\nPreço Base = NºBases * Preço cm² base * π * Raio^2" +
          f"\nPreço Base = {numeroBases} * {precoBase_float} * {valor_pi:.3} * {raio}^2 + {precoLado_float} * 2 * {valor_pi:.2} * {raio} * {altura:.4}" +
          f"\nPreço Base = {(numeroBases*precoBase_float*valor_pi):.3} * {raio**2}" +
          f"\nPreço Base = R${(numeroBases*precoBase_float*valor_pi*raio**2):.4}" +
          f"\n\nPreço Lateral:" +
          "\nPreço Lateral = Preço cm² Lateral * 2 * π * raio * altura" +
          f"\nPreço Lateral = {precoLado_float} * 2 * {valor_pi:.3} * {raio:.3} * {altura}" +
          f"\nPreço Lateral = {(precoLado_float*2*valor_pi*raio*altura):.4}" +
          "\n\nPreço Total = Preço Lateral + Preço Base" +
          f"\nPreço Total = {TotalLado:.4} + {TotalBase:.4}" +
          f"\nPreço Total = {(TotalLado+TotalBase):.4}")

    while option < 0 or option > 1:
        option = int(input("\nDigite 1 para fazer outra conta ou 0 para sair\nInsira sua escolha: "))

print ( "Programa finalizado!!")
