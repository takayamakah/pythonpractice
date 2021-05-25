import pycep_correios 
from pycep_correios.exceptions import CEPNotFound, InvalidCEP

#Captura cep na tela
cep = input('Digite o cep: ').replace('-','').replace('.','').replace(' ','')

try:
    #busca endereço com a biblioteca pycep_correios
    endereco = pycep_correios.get_address_from_cep(cep)    
    
    #Imprime cep válido e endereço completo
    print('CEP válido!')
    print(endereco)

#Se ocorrer um erro CEPNotFound ou InvalidCEP, imprime mensagem
except CEPNotFound or InvalidCEP:
    print('CEP não encontrado ou CEP inválido!')
