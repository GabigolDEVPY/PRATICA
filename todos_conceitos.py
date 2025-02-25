import os
import random
from decimal import Decimal

# Limpa a tela
os.system('cls')

# Tipos básicos
print("Hello World!")  # print
nome = "Gabriel"  # Tipo str (string)
idade = 30  # Tipo int
altura = 1.75  # Tipo float
is_programmer = True  # Tipo bool (boolean)
saldo = Decimal('100.50')  # Usando Decimal para precisão em números

# Coerção de tipos
print("A idade é " + str(idade))  # Coerção para string

# Concatenação e repetição com operadores aritméticos
print(nome + " Rocha")  # Concatenação
print(nome * 3)  # Repetição

# Ellipsis
nada = ...
print(nada)  # Ellipsis

# F-strings
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Entrada de dados
entrada = input("Digite algo: ")

# Condicionais if/elif/else
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 60:
    print("Adulto")
else:
    print("Idoso")

# Operadores relacionais e lógicos
if idade >= 18 and altura >= 1.60:
    print("Pode entrar na montanha-russa")
elif not is_programmer or idade < 18:
    print("Acesso negado")
else:
    print("Entrada VIP")

# 'in' e 'not in'
if 'G' in nome:
    print("A letra G está no nome.")
if 'x' not in nome:
    print("A letra x não está no nome.")

# Interpolação com %
print("Nome: %s, Idade: %d" % (nome, idade))

# Fatiamento de strings e len
print(nome[0:3])  # Fatia os três primeiros caracteres
print(len(nome))  # Tamanho da string

# Try/except para capturar erros
try:
    divisao = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")

# Flags, is, is not, None
flag = None
if flag is None:
    print("Flag é None")
if flag is not None:
    print("Flag não é None")

# Loop while com break e continue
contador = 0
while contador < 10:
    if contador == 5:
        break
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

# while / else
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Final do loop while")

# Loop for com range
for i in range(5):
    print(i)

# Lista (list)
lista = [1, 2, 3]
lista.append(4)
print(lista)

# Concatenando e estendendo listas
lista2 = [5, 6, 7]
lista.extend(lista2)
print(lista)

# Cuidados com listas mutáveis
lista_copy = lista.copy()
lista_copy.append(8)
print(lista)  # Original não muda
print(lista_copy)  # Cópia muda

# Tupla (tuple) e desempacotamento
tupla = (10, 20, 30)
a, b, c = tupla
print(a, b, c)

# enumerate para iterar com índice
for i, valor in enumerate(lista):
    print(f"Índice {i}, valor {valor}")

# split, join, strip
frase = "  Olá Mundo  "
palavras = frase.strip().split()
print(palavras)
frase_unida = " ".join(palavras)
print(frase_unida)

# Operação ternária
status = "Menor" if idade < 18 else "Maior"
print(status)

# Função que gera CPF
def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    return cpf

print(f"CPF gerado: {gera_cpf()}")

# Definindo funções
def soma(a, b=10):
    return a + b

print(soma(5))

# *args para argumentos variáveis
def soma_varios(*args):
    return sum(args)

print(soma_varios(1, 2, 3))

# Closure
def saudacao(msg):
    def interno():
        print(msg)
    return interno

saudacao_func = saudacao("Olá!")
saudacao_func()

# Dicionário (dict)
dicionario = {"nome": "Gabriel", "idade": 30}
print(dicionario["nome"])

# Métodos úteis para dict
dicionario.update({"cidade": "São Paulo"})
print(dicionario.keys())
print(dicionario.values())

# Shallow copy vs deep copy
import copy
dict_copy = copy.deepcopy(dicionario)
print(dict_copy)

# Gerando número aleatório
numero_random = random.randint(1, 100)
print(f"Número aleatório: {numero_random}")

# Imprimindo nome ao contrário
print(nome[::-1])
