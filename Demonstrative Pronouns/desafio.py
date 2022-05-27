'''
Codigo de perguntas e respostas para aprimorar o aprendizado dos Pronomes 
Demonstrativos (Demonstrative Pronouns)
'''
import pandas as pd
from random import choice

url_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTYnk1dsVTyXxx9-2mbarCEayKhozmJMFoLH3mTE7gl_mL2uZBrHuEXudqUuAxpzcNHxMNagLMDmpON/pub?output=csv'
'''
Arquivo no Google Drive com Perguntas e Respostas genericas e especificas sobre 
Dicionarios
'''
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
