#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    word1=input('Слово 1? ')
    word2=input('Слово 2? ')

    for letter in set(word1): print(letter,['Нет','Да'][letter in word2])