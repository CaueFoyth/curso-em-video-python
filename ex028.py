import random

numero_gerado = random.randint(0,5)

print("Foi gerado um número aleatório de 0 a 5")
resposta = int(input("Tente adivinhar: "))

if resposta == numero_gerado:
    print("Parabéns você acertou!")
    
else: 
    print("Você errou!")