import validators

endereco = input('Validar URL: ')

if validators.url(endereco):
    print('URL válida!')
else:    
    print('URL inválida!')

