'''
Crie um sistema de perguntas e respostas que interage com o usuário, 
pedindo que o mesmo insira uma resposta. 
Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto 
e para para a proxima pergunta, caso incorreta, 
exiba uma mensagem de erro e pule para a proxima pergunta. Dicts.
'''
import pandas as pd
from random import choice

url_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTYnk1dsVTyXxx9-2mbarCEayKhozmJMFoLH3mTE7gl_mL2uZBrHuEXudqUuAxpzcNHxMNagLMDmpON/pub?output=csv'

def importa_planilha(colunas):
    return pd.read_csv(url_file, index_col=0, header=0, usecols=colunas).to_dict('index')

colunas = list(['ID', 'Perguntas', 'Respostas'])

dd = importa_planilha(colunas)

colunas.remove('ID')

resp_pron = 0

while resp_pron == 0:
    for i in dd.values():
        pergunta = choice(i["Perguntas"])
        print('=-' * 45)
        print(pergunta)
        print("=-" * 45)
        resp = input("Digite sua Resposta: ").strip().title()

        if resp == i['Respostas']:
            print("=-" * 45)
            print("PARABENS VOCE ACERTOU")
            print("=-" * 45)
            resp_pron += 1
        else:
            print("=-" * 45)
            print("PUXA QUE PENA - TENTE NOVAMENTE!")
            print("=-" * 45)
