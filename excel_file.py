import pandas

#Captura na tela caminho do arquivo a ser lido
path_file = input('Qual caminho do arquivo? ')
df = pandas.read_excel(path_file)

print(df)



