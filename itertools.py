import itertools

def condicao(x):
    return x < 40

def main():
    #cycle
    pessoas = ['Jéssica', 'Letícia', 'Gustavo', 'Valentina', 'Davi', 'Kauê']
    ciclo = itertools.cycle(pessoas)
    for i in [1,2,3,4,5,6,7,8]:
        print('Ciclo:', i, next(ciclo))

    #count
    contador = itertools.count(100, 10)
    for i in [1,2,3,4,5,6,7,8]:
        print('Contador:', next(contador))

    #accumulate
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores)
    acumulado = list(acumulado)
    print('Último acumulado:', acumulado[len(valores)-1])

    #Cadeia
    cadeia = itertools.chain('ABCD', '1234')
    print('Chain:', list(cadeia))

    #dropwhile and takewhile
    print('DropWhile: ', list(itertools.dropwhile(condicao, valores)))
    print('TakeWhile: ', list(itertools.takewhile(condicao, valores)))


if __name__ == '__main__':
    main()