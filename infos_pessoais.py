import os

def limpar():
    os.system('cls')
    return limpar

criarlogin = input('Crie um login: ').lower()
criarsenha = input('Crie uma senha: ')
limpar()
tamanho_veste = ''

while True:
    nome = input('Digite seu nome: ')
    limpar()
    login = input('Digite seu login: ').lower()
    senha = input('Digite sua senha: ')
    limpar()
    if login == criarlogin and senha == criarsenha:
        limpar()
        print('ACESSO LIBERADO!')
        idade = int(input('Digite sua idade: '))
        if idade < 18:
            limpar()
            print('Você não tem idade o suficiente!')
            fechar = input('PRESSIONE ENTER PARA ENCERRAR...')
            break
        while True:
            peso = float(input('Digite seu peso em kilos: '))
            altura = float(input('Digite sua altura: '))
            if altura <= 1.60 and peso <= 60:
                tamanho_veste = 'P'
            elif altura <= 1.70 and peso <= 70:
                tamanho_veste = 'M'
            elif altura <= 1.80 and peso <= 80:
                tamanho_veste = 'G'
            elif altura <= 1.90 and peso <= 90:
                tamanho_veste = 'GG'
            elif altura <= 2.00 and peso <= 100:
                tamanho_veste = 'XGG'
            else:
                print('Não encontramos o seu tamanho!')
                continue
            print(
                f"Seu nome é {nome} e sua idade é {idade} anos\n"
                f"seu nome tem {len(nome)} letras\n"
                f"seu nome de trás pra frente é {nome[::-1]}\n"
                f"A primeira letra do seu nome é {nome[0]}\n"
                f"A última letra do seu nome é {nome[-1]}\n"
                f"Seu tamanho de roupa é {tamanho_veste}\n"
                )
            fechar = input('PRESSIONE ENTER PARA ENCERRAR...')
            break
    else:
        print('LOGIN E SENHA ERRADOS, TENTE NOVAMENTE!')
        continue    