print("Vamos descobrir se os números informados para retas conseguem formar um triângulo!")
a = int(input("Informe o primeiro número: "))
b =  int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print("Os números informados pode fazer um triâgulo")
else:
    print("Os números informados não podem formar um triângulo")