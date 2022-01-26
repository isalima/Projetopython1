nota1 = int(input("Entre com a nota 1: \n"))
nota2 = int(input("Entre com a nota2: \n"))

if nota1 < 0 or nota2 < 0:
    print("1 - A nota nao pode ser menor que 0")
elif nota1 > 10 or nota2 > 10:
    print("1 - A nota nao pode ser maior que 10")
else:
    print(f'A media entre as duas notas e {float(nota1 + nota2) / 2}')



