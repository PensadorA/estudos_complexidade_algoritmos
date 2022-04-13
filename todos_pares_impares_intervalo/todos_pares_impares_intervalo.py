
intervalo = int(input('Digite o intervalo desejado'))  # Intervalo informado pelo usuário


def pares_impares(intervalo1):
    numero_par = []
    numero_impar = []
    for i in range(intervalo1):  # For que irá percorrer o intervalo informado
        if i % 2 == 0 and i != 0:  # Verifica se o resto é == 0 e i diferente de 0
            numero_par.append(i)
        else:
            numero_impar.append(i)  # Se o if não identifcar um par, temos um ímpar.
    return numero_par, numero_impar  # retorno das listas (par e ímpar)


print(pares_impares(intervalo))
