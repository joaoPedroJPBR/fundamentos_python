#Funções
ferias = True

def validar_ferias (vacation):
    
    if vacation == True:
        mensagem = 'Você está de férias!'
        ferias = True
    else:
        mensagem = 'Você não está de férias!'
    
    return ferias, mensagem

print(f"Ferias {ferias}")
print(validar_ferias(ferias))#chamando a funcao validar_ferias

ferias = True
  
def validar_ferias (vacation: bool, dias: int):
    
     if vacation == True:
         mensagem = 'Você está de férias por {} dias!'.format(dias)
         ferias = True
     else:
         mensagem = 'Você não está de férias!'
    
     return ferias, mensagem

mens, ferias = validar_ferias(ferias, 30)#chamando a funcao validar_ferias


if __name__ == '__main__':
    validar_ferias(False)