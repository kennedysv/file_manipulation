with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input("Digite o Ano Para Consultar: ")

    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos+float(lista[3])
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros+float(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]

    print("O Total de Voos é: ", total_voos)

    print("O Mês/Ano de Maior Movimento no Aeroporto foi: ",
          str(mes), "/", str(ano))
    print("Total de Passageiros do Ano: ",
          ano_usuario, "Foi de ", total_passageiros)
    print("Mês do Ano ", ano_usuario,
          "com Maior Média para Diária de Hotel foi: ", mes_maior_diaria)
