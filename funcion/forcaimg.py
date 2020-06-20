def forca(x=0, j='null'):
    '''

        -> Verifica numero de erros e imprime boneco na tela

    '''
    if  x==0:
        print('------------     ')
        print('|          |   ')
        print('|             ')
        print('|               ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if x==1:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|               ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if x==2:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|          |     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if  x==3:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if  x==4:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if x==5:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|         /      ')
        print('|           ')
        print('|         ')
        print('|         ')
    if x==6:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|         / \     ')
        print('|           ')
        print('|        ')
        print('|')


def telainicial():
    '''
    Gera Titulo da tela Inicial do Jogo
    '''

    print(f'       _  ____   _____  ____  ')
    print(f'      | |/ __ \ / ____|/ __ \ ')
    print(f'      | | |  | | |  __| |  | |')
    print(f'  _   | | |  | | | |_ | |  | |')
    print(f' | |__| | |__| | |__| | |__| |')
    print(f'  \____/ \____/ \_____|\____/ ')
    print('')
    print(f'           _____          ')
    print(f'          |  __ \   /\    ')
    print(f'          | |  | | /  \   ')
    print(f'          | |  | |/ /\ \  ')
    print(f'          | |__| / ____ \ ')
    print(f'          |_____/_/    \_\\')
    print('')
    print(f'______ ____  _____   _____          ')
    print(f'|  ____/ __ \|  __ \ / ____|   /\    ')
    print(f'| |__ | |  | | |__) | |       /  \   ')
    print(f'|  __|| |  | |  _  /| |      / /\ \  ')
    print(f'| |   | |__| | | \ \| |____ / ____ \ ')
    print(f'|_|    \____/|_|  \_\\_____/_/    \_\\')