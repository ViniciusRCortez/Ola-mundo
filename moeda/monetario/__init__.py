from moeda import menu


def metade(n=0, moeda='R$', f=True):
    n /= 2
    if f:
        n = formatar(n, moeda)
    return n


def dobro(n=0, moeda='R$', f=True):
    n *= 2
    if f:
        n = formatar(n, moeda)
    return n


def aumentar(n=0, i=0, moeda='R$', f=True):
    n *= (1+(i/100))
    if f:
        n = formatar(n, moeda)
    return n


def diminuir(n=0, i=0, moeda='R$', f=True):
    i *= -1
    r = aumentar(n, i, moeda, f)
    return r


def formatar(n=0, moeda='R$'):
    n = str(f'{n:.2f}')
    n = n.replace('.', ',')
    return f'{moeda}{n}'


def resumo(v=0, a=0, d=0, f=True):
    menu('Resumo', 42)
    print(f'A metade de {formatar(v)} é \t{metade(v,f= f)}')
    print(f'O dobro de \t{formatar(v)} é \t{dobro(v, f=f)}')
    print(f'{formatar(v)} aumentado em \t{a}% é \t{aumentar(v, a, f=f)}')
    print(f'{formatar(v)} diminuido em \t{d}% é \t{diminuir(v, d, f=f)}')
