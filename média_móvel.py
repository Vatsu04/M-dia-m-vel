casos = []

msg = "Com quantos numeros você gostaria de calcular a média móvel? "
numeros = int(input(msg))

while True:
    casos.insert(0,int(input("Casos:")))
    if len(casos) > numeros:
        casos.pop()
    soma = 0
    for i in range(len(casos)):
        soma += casos[i]
    mm = soma/len(casos)

    print(casos, round(mm,2))

    