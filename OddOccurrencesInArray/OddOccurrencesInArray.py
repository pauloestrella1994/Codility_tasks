# -*- coding: utf-8 -*-


def solution(A):
    result = 0
    for i in A:
        result ^= i #comando XOR que compara os valores em binario e retorna o exclusivo
    return result



