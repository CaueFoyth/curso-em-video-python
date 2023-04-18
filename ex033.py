print("Vamos descobrir qual número é o maior e o menor!")
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o tercerio número: "))

if n2 < n1 > n3:
    print(f"O maior número é {n1}!")
elif n1 < n2 > n3: 
    print(f"O maior número é {n2}!")
elif n1 < n3 > n2:
    print(f"O maior número é {n3}!")

if n2 > n1 < n3: 
    print(f"O menor número é {n1}!")
elif n1 > n2 < n3:
    print(f"O menor número é {n2}!")
elif n1 > n3 < n2:
    print(f"O menor número é {n3}!")