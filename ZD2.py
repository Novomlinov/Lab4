#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input()
    for i, a in enumerate(s[:-1]):
        if a == s[i + 1]:
            print(i, i + 1)
            break
    else:
        print('соответствующее сообщение')