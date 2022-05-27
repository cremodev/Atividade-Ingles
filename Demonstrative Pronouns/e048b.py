'''
Crie um sistema de perguntas e respostas que interage com o usuário, 
pedindo que o mesmo insira uma resposta. 
Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto 
e para para a proxima pergunta, caso incorreta, 
exiba uma mensagem de erro e pule para a proxima pergunta. Dicts.
'''
import pandas as pd
from random import choice

#from traitlets import DottedObjectName

def sorteia(dd):
    ''' Retorna item aleatorio do dicionaro dicionario de dados em ordem aleatoria     
    '''
    t = 'ok'
    while t == 'ok':
        try:
            newdd = (choice(dd))
            t = 'foi'
        except:
            pass
    return newdd


def importa_planilha(colunas):
    '''Retorna cvs google sheets para dict'''
    url_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTYnk1dsVTyXxx9-2mbarCEayKhozmJMFoLH3mTE7gl_mL2uZBrHuEXudqUuAxpzcNHxMNagLMDmpON/pub?output=csv'
    return pd.read_csv(url_file, index_col=0, header=0, usecols=colunas).to_dict('index')

def ln():
    for i in range(30):       
        print('-', end='')
    print()
    
colunas = list(['ID', 'Perguntas', 'Respostas'])
dd = importa_planilha(colunas)

resp_pron = 0
resp = ''
qtd_perguntas = 0

while resp != '999':
    qtd_perguntas += 1
    uma_pergunta = sorteia(dd)
    pergunta = uma_pergunta['Perguntas']
    resposta_certa = uma_pergunta['Respostas']

    ln()
    print(pergunta)
    ln()

    resposta_certa = str(resposta_certa).strip().upper()
    # print("Resposta certa é:", resposta_certa)
    resp = input("Digite sua Resposta ou 999 para sair: ").strip().title()
    resp = str(resp).strip().upper()

    # print('Resposta digitada foi: ', resp)

    ln()
    if resp == resposta_certa:
        resp_pron += 1
        print("PARABENS VOCE JÁ ACERTOU ", resp_pron, " Perguntas")
    else:
        print("PUXA QUE PENA - TENTE NOVAMENTE!")

    ln()

ln()
print(
    f'Voce testou {qtd_perguntas} Perguntas, acertou {resp_pron} e errou { qtd_perguntas - resp_pron}')
ln()