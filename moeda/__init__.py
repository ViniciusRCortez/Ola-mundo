def menu(msg, n=0, tipo=0):
    """
    Cria cabeçario com um texto pra organização
    :param msg: Texto central do cabeçario
    :param n: Cor da letra
    :param tipo: Se vair ser negrito(1) ou Italico(2)
    by Vinicius R. Cortez
    """
    if tipo == 0:
        print(f'\033[30;{n}m-' * 40)
        print(f'\033[30;{n}m{msg:^40}')
        print(f'\033[30;{n}m-' * 40)
        print('\033[m', end='')
    else:
        print(f'\033[30;{n};{tipo}m-'*40)
        print(f'\033[30;{n};{tipo}m{msg:^40}')
        print(f'\033[30;{n};{tipo}m-'*40)
        print('\033[m', end='')


def ListaOpc(list):
    """
    Cria um menu com uma lista de opçoes enumeradas de 1 ao len(list)
    :param list: lista de opçoes desejadas
    by Vinicius R. Cortez
    """
    c = 1
    print(f'\033[30;33m-' * 40)
    for item in list:
        print(f'\033[30;33m{c}:\t{item}\033[m')
        c += 1
    print(f'\033[30;33m-' * 40)
    print('\033[m', end='')
