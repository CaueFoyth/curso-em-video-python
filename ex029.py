velocidade = int(input("Informe quantos Km/h você está: "))
if velocidade >= 80:
    preco_multa = (velocidade - 80) * 7
    print(f"Você levou uma multa de R${preco_multa},00")