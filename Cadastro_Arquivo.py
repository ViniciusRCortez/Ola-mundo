from moeda import menu, ListaOpc
from moeda.dado import leiaInt

lista = ['Verificar cadastros', 'Cadastrar nova pessoa', 'Encerrar programa']
# Ultima opção deve ser Encerrar programa sempre
while True:
    # Escreve o menu de opções
    menu('Menu principal', 32, 1)
    ListaOpc(lista)

    while True:
        # Valida a opção op lida
        op = leiaInt(input('\033[34mDigite sua opção: \33[m'))
        if len(lista) >= op >= 1:
            break
        print('\033[31mOpção invalida, tente novamente.\033[m')
    menu(f'Opção {op} ', 32)

    if op == len(lista):
        # Fecha Programa
        print('\033[33mOBRIGADO, VOLTE SEMPRE :)\033[m')
        break

    if op == 1:
        # Ecreve linha por linha
        try:
            arquivo = open('Curso_em_Video.txt', 'r')
            linha = arquivo.readline()
            print('-'*40)
            while linha:
                linha = linha.split()
                try:
                    v = int(linha[1])
                except:
                    print(f'  NOME: {f"{linha[0]} {linha[1]}":<15}\tIDADE: {linha[2]}')
                else:
                    print(f'  NOME: {linha[0]:<15}\tIDADE: {linha[1]}')
                linha = arquivo.readline()
            print('-'*40)
            arquivo.close()
        except:
            print('Arquivo vazio')

    if op == 2:
        # Cria uma linha nova no Curso_Em_Video.txt
        arquivo = open('Curso_em_Video.txt', 'a')
        cadastro = []
        cadastro.append(input('Nome: '))
        cadastro.append(' ')
        cadastro.append(input('Idade: '))
        cadastro.append('\n')
        arquivo.writelines(cadastro)
        cadastro.clear()
        arquivo.close()
