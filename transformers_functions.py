def filter_first(x):
    if x % 2 == 0:
        return False
    return True

def filter_second(x):
    if x.isupper():
        return False
    return True

def filter_third(x):
    if x.isupper():
        return True
    return False

def square(x):
    return x**2

def note_concept(x):
    if x >= 90:
        return 'A'
    elif x >= 80 and x < 90:
        return 'B'
    elif x >= 70 and x < 80:
        return 'C'
    elif x >= 60 and x < 70:
        return 'D'
    return 'F'

def main():
    numeros = (1,8,4,5,13,26,381,410,58,47)
    letras = 'abcDeFGHiJklmnoP'
    notas = (81,89,94,78,61,66,99,74,60,59)
    
    impares = list(filter(filter_first, numeros))
    print('Números Ímpares:', impares)

    minusculas = list(filter(filter_second, letras))
    print('Letras Maiúsculas:', minusculas)

    maiusculas = list(filter(filter_third, letras))
    print('Letras Mínusculas:', maiusculas)

    quadrados = list(map(square, numeros))
    print(quadrados)

    #notas = sorted(notas)
    conceitos = list(map(note_concept, notas))
    print(conceitos)

if __name__ == "__main__":
    main()
