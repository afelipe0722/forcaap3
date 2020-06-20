# -*- coding: utf-8 -*-
"""
Esse é o arquivo com a função responsável por sortear as palavras e dicas
"""
import random


def sortpalavra():
    '''
    ->Gera um numero randômico e procura no arquivo utils/dica.txt qual palavra e
    dica que corresponde a numero gerado

    -------
    vretorno :  RETORNA STRING NO FORMATO 'PALAVRA-DICA' COM A PALAVRA E
        DICA ENCONTRADA NO TXT

    '''

    # gera numero randomico
    nrodica = random.randrange(1, 30)
    arquivo = open('utils/dica.txt', 'r')
    dados = list()

    # procura numero randômico gerado no arquivo da variável 'arquivo'
    for linha in arquivo:
        vlista = linha.split('-')
        dados.append(vlista)

        for x in range(0, len(dados)):
            vnrdica = int(dados[x][0])
            if vnrdica == nrodica:
                vpalavra = dados[x][1]
                vdica = dados[x][2]
    # fecha arquivo
    arquivo.close()

    # joga palavra e dica encontrada no txt para a variavel vretorno
    vretorno = vpalavra + '|' + vdica

    return vretorno
