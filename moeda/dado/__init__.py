def leiaDin(v):
    """
       Valida uma string e a transforma em real, repete até receber um real valido
       :param v: String a ser validada
       :return: float(v)
       By Vinicius R. Cortez
    """
    while True:
        v = v.replace(',', '.').strip()
        try:
            v = float(v)
        except KeyboardInterrupt:
            print('\033[31mValor imterrompido\033[m')
        except (TypeError, ValueError):
            v = input('\033[31mValor invalido\033[m\nDigite outro valor R$')
        else:
            print('NUMERO REAL VALIDADO')
            break
    return float(v)

def leiaInt(v):
    """
    Valida uma string e a transforma em inteiro, repete até receber um inteiro valido
    :param v: String a ser validada
    :return: int(v)
    By Vinicius R. Cortez
    """
    while True:
        try:
            v = int(v)
        except KeyboardInterrupt:
            print('\033[31mValor imterrompido\033[m')
        except (TypeError, ValueError):
            v = input('\033[31mValor invalido\033[m\n\033[34mDigite outro valor: \033[m')
        else:
            # print('\33[34mNUMERO INTEIRO VALIDADO\033[m')
            break
    return int(v)

