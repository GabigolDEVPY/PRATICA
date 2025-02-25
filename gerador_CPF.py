import random

vezes = int(input('Quantos CPFs você quer gerar ?: '))

for interacao in range(vezes):
    nove_digitos = ''
    primeiro_digito = 0
    contador_regressivo = 10 

    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    for digito in nove_digitos:
        primeiro_digito += int(digito) * contador_regressivo
        contador_regressivo -= 1
    primeiro_digito = primeiro_digito * 10 % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0  

    nove_digitos = nove_digitos + str(primeiro_digito)

    contador_regressivo = 11
    segundo_digito = 0

    for digito in nove_digitos:
        segundo_digito += int(digito) * contador_regressivo
        contador_regressivo -= 1
    segundo_digito = segundo_digito * 10 % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0 

    nove_digitos += str(segundo_digito)
    print(nove_digitos)