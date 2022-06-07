import pandas as pd
from random import choice


print('''\033[;1mHello, this is an exercise to test your skills with Demonstrative Pronouns
Fill in the blanks with [THIS-THAT-THESE-THOSE]\033[m ''')
print('-=-'*20)

def sorteia(dd):
    t = 'ok'
    while t == 'ok':
        try:
            newdd = (choice(dd))
            t = 'foi'
        except:
            pass
    return newdd


def importa_planilha(colunas):
    url_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTYnk1dsVTyXxx9-2mbarCEayKhozmJMFoLH3mTE7gl_mL2uZBrHuEXudqUuAxpzcNHxMNagLMDmpON/pub?output=csv'
    return pd.read_csv(url_file, index_col=0, header=0, usecols=colunas).to_dict('index')

def ln():
    for i in range(20):       
        print('-=-', end='')
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

    print(pergunta)
    ln()

    resposta_certa = str(resposta_certa).strip().upper()
    resp = input("Answer with the proper pronoun or type 999 to exit: ").strip().title()
    resp = str(resp).strip().upper()


    ln()
    if resp == resposta_certa:
        resp_pron += 1
        print(f"\033[1;32mCONGRATS YOU ALREADY GET {resp_pron} ANSWERS RIGHT\033[m")
    else:
        print("\033[1;31mWHAT A SHAME ... GOOD LUCK NEXT TIME\033[m")

    ln()


print(
    f'You tested {qtd_perguntas} questions, \033[1;32mnailed {resp_pron}\033[m and \033[1;31mmissed { qtd_perguntas - resp_pron}\033[m')
ln()
