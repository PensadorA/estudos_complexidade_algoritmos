import random
lista_inteiros = random.sample(range(0, 90), 5)


def valor_max(lista_dados):
    maximo = lista_inteiros[0]
    for i in lista_dados:
        if i > maximo:

            maximo = i
    return maximo


print(lista_inteiros)
print(valor_max(lista_inteiros))


