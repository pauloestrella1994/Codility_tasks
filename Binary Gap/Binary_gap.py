# -*- coding: utf-8 -*-

def solutions(N):
    return len(max(str(bin(n))[2:].strip('0').strip('1').split('1')))

#comando len lê o tamanho de uma string e retorna um inteiro
#comando max retorna o maximo de um valor
#bin retorna o binario de uma entrada
#strip retira a sequencia de valores das extremidades, caso haja, do valor O e 1
#split utiliza o valor 1 como separador do binario, desmontando a estrutura e retornando uma lista de intervalos (splits)