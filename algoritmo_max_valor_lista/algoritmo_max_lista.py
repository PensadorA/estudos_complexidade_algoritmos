import random
lista_inteiros = random.sample(range(0, 9000), 100)  # lista randômica de 10 números inteiros entre 0 e 100


def valor_max(lista_dados):  # Implementar do algoritmo número máximo de uma lista
    """
    Função que implementar algoritmo de máximo de uma lista
    :param lista_dados: list
    :return max: int
    """
    maximo = lista_inteiros[0]  # váriavle para acumular, tomemos o primeiro elemento da lista como valor máximo
    for i in lista_dados:  # laço para percorrer a lista
        if i > maximo:  # Estrutura condicional, caso i que está sendo percorrido na lista seja maior que o valor de maximo, execute o escopo local
            maximo = i  # Atualiza o valor de maximo
    return maximo  # retorna maximo para quem o chamou


print(lista_inteiros)
print(valor_max(lista_inteiros))


