print('Vou contar quantas vezes a palavra apareceu!')
texto = input('Digite o texto: ').lower()

vezes_apareceu = 0
letra_apareceu_mais = ''

for letra in texto:
    if letra == ' ':
        continue
    vezes_apareceu_mais_atual = texto.count(letra)

    if vezes_apareceu <= vezes_apareceu_mais_atual:
        vezes_apareceu = vezes_apareceu_mais_atual
        letra_apareceu_mais = letra

print(f'A letra que apareceu mais foi {letra_apareceu_mais} que apareceu {vezes_apareceu} vezes') 