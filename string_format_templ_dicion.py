from string import Template

def getFormatacaoCondicional(par_aluno, par_curso, par_professor):   
    frase = '{0}, você está assistindo {1} com {2}!'.format(par_aluno, par_curso, par_professor)
    print(frase) 

def getTemplate(par_aluno, par_curso, par_professor):
    templ = Template('${aluno}, você está assistindo ${curso} com ${professor}!')
    frase = templ.substitute(aluno=par_aluno, curso=par_curso, professor=par_professor)
    print(frase) 

def getDicionarioDados(par_aluno, par_curso, par_professor):
    dados = {"aluno": par_aluno, "curso": par_curso, "professor": par_professor}
    templ = Template('${aluno}, você está assistindo ${curso} com ${professor}!')
    frase = templ.substitute(dados)
    print(frase) 


aluno = 'Karine Takayama'#input('Nome do Aluno: ')
curso = 'Python Avançado'#input('Nome do Curso: ')
professor = 'Jéssica Temporal'#input('Nome do Professor: ')

#Formatação Condicional
print('Formatação Condicional')
getFormatacaoCondicional(aluno, curso, professor)

print('')

#Template
print('Template')
getTemplate(aluno, curso, professor)
print('')

#Dicionário de Dados
print('Dicionário de Dados')
getDicionarioDados(aluno, curso, professor)


