km = int(input("Informe a distância da viagem: "))
if km <= 200:
    print(f"O preço da passagem será R${km*0.50}")
else:
    print(f"O preço da passagem será R${km*0.45}")