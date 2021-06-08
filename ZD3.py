#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    word = input()
    result = [word[0]]
    for char in word[1:]:
        if char != result[-1]:
            result.append(char)

    print(''.join(result))