import math
option = -1
while not option == 0:
    option = -1
    distanciaAgua_string = "-1"
    distanciaAgua_float = 1

    while distanciaAgua_string.startswith("-") or not distanciaAgua_string.endswith("m") or distanciaAgua_float < 0:
        distanciaAgua_string = "-1"
        distanciaAgua_float = 1

        print("Digite o largura da margem do rio em metros  e positivo, exemplo: 25,0690m")
        distanciaAgua_string = str(input("Insira o valor aqui:")).lower()
        distanciaAgua_string = distanciaAgua_string.replace(",", ".")
        distanciaAgua_string = distanciaAgua_string.replace(" ", "")

        if not distanciaAgua_string.endswith("m"):
            print("Valor inválido!!Digite um valor válido!")

        try:
            distanciaAgua_float = float(distanciaAgua_string[:-1])
        except ValueError:
            print("Valor com digitos a mais!!")

        if distanciaAgua_float < 0:
            print("Valor negativo invalido!!")

    distanciaTerra_string = "-1"
    distanciaTerra_float = 1

    while distanciaTerra_string.startswith("-") or not distanciaTerra_string.endswith("m") or distanciaTerra_float < 0 :
        distanciaTerra_string = "-1"
        distanciaTerra_float = 1

        print("Digite o distância até a fábrica por terra, exemplo: 25,0690m")
        distanciaTerra_string = str(input("Insira o valor aqui:")).lower()
        distanciaTerra_string = distanciaTerra_string.replace(",", ".")
        distanciaTerra_string = distanciaTerra_string.replace(" ", "")

        if not distanciaTerra_string.endswith("m"):
            print("Valor inválido!!Digite um valor válido!")

        try:
            distanciaTerra_float = float(distanciaTerra_string[:-1])
        except ValueError:
            print("Valor com digitos a mais!!")

        if distanciaTerra_float < 0:
            print("Valor negativo invalido!!")

    precoAgua_string = "-1"
    precoAgua_float = 1

    while (not precoAgua_string.startswith("r$")) or precoAgua_float < 0:
        print("Digite o preço do metro do cabo pelo rio, exemplo: R$1,50")
        precoAgua_string = str(input("Insira o valor aqui:")).lower()
        precoAgua_string = precoAgua_string.replace(",", ".")
        precoAgua_string = precoAgua_string.replace(" ", "")

        if not precoAgua_string.startswith("r$"):
            print("Valor inválido!!Digite um valor válido!")
        try:
            precoAgua_float = float(precoAgua_string[2:])
        except ValueError:
            print("Valor com digitos a mais!!")
        if precoAgua_float < 0:
            print("Valor negativo invalido!!")

    precoTerra_string = "-1"
    precoTerra_float = 1

    while (not precoTerra_string.startswith("r$")) or precoTerra_float < 0 or precoTerra_float >= precoAgua_float:
        print("Digite o preço do metro de cabo por terra, exemplo: R$1,50\nOBS: preço TEM que ser menor que o pela água(motivos matemáticos de domínio)")
        precoTerra_string = str(input("Insira o valor aqui:")).lower()
        precoTerra_string = precoTerra_string.replace(",", ".")
        precoTerra_string = precoTerra_string.replace(" ", "")

        if not precoTerra_string.startswith("r$"):
            print("Valor inválido!!Digite um valor válido!")
        try:
            precoTerra_float = float(precoTerra_string[2:])
        except ValueError:
            print("Valor com digitos a mais!!")

        if precoTerra_float >= precoAgua_float:
            print("O preço do cabo por terra tem que ser menor que o por sobre o rio!!\n")
        elif precoTerra_float < 0:
            print("Valor negativo invalido!!")


    deltaDistancia = math.sqrt((precoTerra_float**2 * distanciaAgua_float**2)/(precoAgua_float**2-precoTerra_float**2))
    percorridoAgua = math.sqrt(distanciaAgua_float**2 + deltaDistancia**2)
    percorridoTerra = distanciaTerra_float - deltaDistancia

    print("\n\n\tCalculos:" +
          "\nDelta Distância:" +
          "\nDelta Distância = ((Preço Fio por terra² * Distância Margem Rio²) / (Preço fio sobre o Rio² - Preço Fio por terra²))^(1/2)" +
          f"\nDelta Distância = (({precoTerra_float}² * {distanciaAgua_float}²) / ({precoAgua_float}² - {precoTerra_float}²))^(1/2)" +
          f"\nDelta Distância = (({precoTerra_float**2} * {distanciaAgua_float**2}) / ({precoAgua_float**2} - {precoTerra_float**2}))^(1/2)" +
          f"\nDelta Distância = ({precoTerra_float**2 * distanciaAgua_float **2} / {precoAgua_float**2 - precoTerra_float**2})^(1/2)" +
          f"\nDelta Distância = ({(precoTerra_float**2 * distanciaAgua_float **2) / (precoAgua_float**2 - precoTerra_float**2)})^(1/2)" +
          f"\nDelta Distância = {((precoTerra_float**2 * distanciaAgua_float **2) / (precoAgua_float**2 - precoTerra_float**2))**(1/2)}" +
          "\n\nDistância por água :" +
          "\nDistância por água = (Distância Margem Rio² + Delta Distância)^(1/2)" +
          f"\nDistância por água = ({distanciaAgua_float}² + {deltaDistancia}²)^(1/2)" +
          f"\nDistância por água = ({distanciaAgua_float**2} + {deltaDistancia**2})^(1/2)" +
          f"\nDistância por água = ({distanciaAgua_float**2 + deltaDistancia**2})^(1/2)" +
          f"\nDistância por água = {(distanciaAgua_float**2 + deltaDistancia**2)**(1/2)}" +
          "\n\nDistância por terra:" +
          "\nDistância por terra = Comprimento por terra - Delta Distância" +
          f"\nDistância por terra = {distanciaTerra_float} - {deltaDistancia}" +
          f"\nDistância por terra = {distanciaTerra_float - deltaDistancia}" +
          "\n\nMenor Preço:" +
          "\nMenor Preço = Preço Fio por terra * Distância por Terra + Preço fio sobre o Rio * Distância Água" +
          f"\nMenor Preço = {precoTerra_float} * {percorridoTerra} + {precoAgua_float} * {percorridoAgua}" +
          f"\nMenor Preço ={precoTerra_float*percorridoTerra} + {precoAgua_float*percorridoAgua}" +
          f"\nMenor Preço ={precoTerra_float*percorridoTerra + precoAgua_float*percorridoAgua}")
    while option < 0 or option > 1:
        option = int(input("\nDigite 1 para fazer outra conta ou 0 para sair\nInsira sua escolha: "))
