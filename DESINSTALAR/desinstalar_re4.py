import pyautogui
import time

import os
def amor():
    print(
    'ADIVINHE O NOME DA SUA GATINHA,\n'
    'DICA: COMEÇA COM G E TERMINA COM GABRIELA'
    )

amor()

palavra_secreta = 'Gabriela'.lower()
letras_acertadas = ''
tentativas = 0
palavra_formada = ''

while True:
    if tentativas > 7:
        print('Você errou o nome do AMOR DA SUA VIDA, FEIO FEIO\n'
            'Você ficará sem seu RESIDENT EVIL 4 REMAKE')
        pyautogui.PAUSE = 2

        time.sleep(2)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.click(x=93, y=671)
        pyautogui.doubleClick(x=243, y=371)
        pyautogui.doubleClick(x=348, y=183)
        pyautogui.doubleClick(x=348, y=183)
        pyautogui.click(x=315, y=266)
        pyautogui.press("Delete")
        pyautogui.click(x=1199, y=1055)
        time.sleep(2)

        print('Pronto, seu re4 foi desinstalado, preste mais atenção da próxima vez!!!!')
        tentar = input('Deseja tentar novamente [S]im ou [N]ão ?: ').lower().startswith('n')
        tentativas = 0
        if tentar:
            break
    letra_digitada = input('Digite uma letra: ').lower()
    if letra_digitada == ' ' or letra_digitada == (''):
        os.system('cls')
        amor()
        print('Digite pelo menos uma letra!')
        print(palavra_formada)
        continue
    if len(letra_digitada) >1:
        os.system('cls')
        amor()
        print('Digite apenas uma letra!')
        print(palavra_formada)
        continue 
    tentativas += 1
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letras in palavra_secreta:
        if letras in letras_acertadas:
            palavra_formada += letras
        else:
            palavra_formada += '*'
    os.system('cls')

    amor()
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(
            f"VOCÊ ACERTOU O NOME DO AMOR DA SUA VIDA!!\n"
            f"E O NÚMERO DE TENTATIVAS FORAM {tentativas} VEZES"
        )
        sair = input('pressione ENTER para sair...')
        break



