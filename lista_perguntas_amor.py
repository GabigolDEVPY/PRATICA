import os
import time

while True:
    print('Jogo de perguntas sobre sua GATINHA!')
    perguntas = [
        {
            'Pergunta': 'Qual a data de aniversário dela ?',
            'Opções': ['11/05', '29/05', '30/05', '32/05'],
            'Resposta': '32/05',
        },
        {
            'Pergunta': 'Qual o chocolate preferido dela ?',
            'Opções': ['Ao leite', 'Meio Amargo', 'Branco', '100% cacau'],
            'Resposta': 'Ao leite',
        },
        {
            'Pergunta': 'Qual treino favorito dela ?',
            'Opções': ['Glúteos', 'Costas e bíceps', 'Ficar em casa dormindo', 'Peito e tríceps'],
            'Resposta': 'Ficar em casa dormindo',
        },
        {
            'Pergunta': 'Qual filmes desses ela mais gosta ?',
            'Opções': ['Alice no país das maravilhas', 'Divertidamente 2', 'Era do gelo ', 'Menino do pijama listrado'],
            'Resposta': 'Divertidamente 2',
        },
        {
            'Pergunta': 'Qual desses apelidos ela odeia te chamar ?',
            'Opções': ['Gatinho', 'Garoto', 'Meu bem', 'Princeso'],
            'Resposta': 'Garoto',
        },
    ]

    qtd_acertos = 0
    for pergunta in perguntas:
        print('Jogo de perguntas sobre sua GATINHA!')
        print()
        print('Pergunta:', pergunta['Pergunta'])
        print()

        opcoes = pergunta['Opções']
        for i, opcao in enumerate(opcoes):
            print(f'{i})', opcao)
        print()

        escolha = input('Escolha uma opção: ')

        acertou = False
        escolha_int = None
        qtd_opcoes = len(opcoes)

        if escolha.isdigit():
            escolha_int = int(escolha) 

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['Resposta']:
                    acertou = True
        print()
        if acertou:
            qtd_acertos += 1
            os.system('cls')
            print("Acertou, parabéns!!! 😉")
            time.sleep(2)
        else:
            print('Errou, espere que ela não veja isso!!! FEIO FEIO')  

        print()      



    if qtd_acertos == len(perguntas):
        print('Você está completamente apaixonado por ela 😍😍😍😍')
        print()
        print('Você acertou', qtd_acertos)
        print('de', len(perguntas), 'Perguntas')
    else:
        print('Você errou coisas simples, ela não está feliz com isso!!!')
        print('Você acertou', qtd_acertos)
        print('de', len(perguntas), 'Perguntas')

    time.sleep(5)












