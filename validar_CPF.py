import random

while True:
    cpf = input('Digite um CPF apenas números: ')
    if len(cpf) != 11:
        print('O CPF não contém 11 digitos')
        continue


    nove_digitos = cpf[:9]
    primeiro_digito = 0
    contador_regressivo = 10 


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

    if nove_digitos == cpf:
        print('CPF válido')
    else:
        print('CPF inválido')    
