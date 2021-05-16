import pycep_correios

#Captura cep em tela
cep = input('Qual o CEP? ')

#Busca endereço com a biblioteca pycep_correios
endereco = pycep_correios.consultar_cep(cep)

#Imprime o endereço por partes
print(endereco['end'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['complemento2'])
print(endereco['uf'])
print(endereco['cep'])
