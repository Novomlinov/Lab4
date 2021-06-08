#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input('Введите строку символов ')
    k = 2
    l = len(s)
    while k < l:
        s2 = s[k]  # Срез строки s
        print(s2)
        k = k + 3