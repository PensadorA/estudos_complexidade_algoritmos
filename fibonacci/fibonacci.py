
qtn_termos = int(input('Quantos termos deseja? '))


def fibonacci(qtn_termos1):  # Função para calcular o énesmo termo da sequeência de fibonacci
    a, b, c = 0, 1, None  # Declação de váriáveis, primeiro e segundo termo, terceira variável de acumulador
    for i in range(qtn_termos1):  # Laço que irá percorrer até atingir o termo desejado.
        c = a + b  # Soma dos dois valores anteriores
        a = b, b = c  # Atualiza os valores dos dois últimos valores.
    return c  # Retorna o énesmo termo


print(fibonacci(qtn_termos))
