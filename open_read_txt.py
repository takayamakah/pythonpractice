#Abrir e ler arquivo txt
def openreadtxt(path_txt):
    with open(path_txt, 'r') as txt:
        for linha in iter(txt.readline, ''):
            print(linha)


#Chama função
path = input('Caminho de Arquivo para leitura: ')
openreadtxt(path)