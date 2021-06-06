#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    word=input('Слово?')
    double=[]
    result=[]

    for letter in word:
      if letter not in double:
        if word.count(letter)>1: double.append(letter)
        result.append(letter)

    print(''.join(result))