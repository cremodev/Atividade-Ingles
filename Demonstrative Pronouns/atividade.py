from dicionario import perguntas

print('''Olá, esse é um exercício para testar suas habilidades com demonstrative pronouns

Temos 8 perguntas para você responder
Preencha os espaços em branco ''')
print('-=-' * 15)

respostas_certas = 0

for pkey, pvalue in perguntas.items():
    print(f'{pkey} : {pvalue["pergunta"]}')
    print('-=-'*13)


    resposta_user = input('Responda com [This ou That]: ').strip().upper()
    print()

    if resposta_user == pvalue["resposta_certa"]:
        print('\033[1;32mPARABÉNS, VOCÊ ACERTOU!!!!\033[m')
        print('-=-'*13)
        respostas_certas += 1
    else:
        print('\033[1;31mRESPOSTA ERRADA, BOA SORTE NA PRÓXIMA\033[m')
        print('-=-'*13)

print('Muito Obrigado por usar nosso programa :)')
