#Funções Iteradoras (enumerate, zip, iter, next)

def iterador_while(language):
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    if language == 'p':
        iterador_dias = iter(dias)
    elif language == 'e':
        iterador_dias = iter(dias_en)
    
    cont = 0
    while (cont <= 6):
        print(next(iterador_dias))
        cont = cont + 1

def iterador_for(language):
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    if language == 'p':
        iterador_dias = iter(dias)
    elif language == 'e':
        iterador_dias = iter(dias_en)
    
    for count in range(len(dias)):
        print(next(iterador_dias))

def iterador_range(language):
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    if language == 'p':
        for numero in range(len(dias)):
            print(numero, dias[numero])
    elif language == 'e':
        for numero in range(len(dias_en)):
            print(numero, dias[numero])

def iterador_enumerate(language):
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    if language == 'p':
        for i, dia in enumerate(dias):
            print(i, dia)
    elif language == 'e':
        for i, dia in enumerate(dias_en):
            print(i, dia)

def iterador_zip():
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    for d in zip(dias, dias_en):
        print(d)

def iterador_enumerate_zip(language):
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    dias_en = ["sun","mon","tue","wed","thu","fri","sat"]
    
    if language == 'p':
        for i, d in enumerate(zip(dias, dias_en)):
            print(i, d[0], "=", d[1], "em Inglês")
    elif language == 'e':
        for i, d in enumerate(zip(dias_en, dias)):
            print(i, d[0], "=", d[1], "em Português")
      
def main():
    #Chama função iterador
    language = input('Language: [p/e] ')
    iterador_enumerate_zip(language)

if __name__ == "__main__":
    main()