import os

lista = []


while True:
    opcao = input('Digite [L]istar [I]nserir [A]pagar: ').lower()

    if opcao == 'i':
        valor = input('Digite um valor: ')
        lista.append(valor)
        os.system('cls')

    elif opcao == 'a':
        indice_str = input('Qual indice deseja apagar ?: ')
        try:
            indice = int(indice_str)
            del lista[indice]
            
        except IndexError:
            print('Esse indice não existe na lista')
        
        except ValueError:
            print('Digite apenas números')

        except Exception:
            print('Erro desconhecido!')    
    elif opcao == 'l':
        if len(lista) < 1:
            print('Nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor )