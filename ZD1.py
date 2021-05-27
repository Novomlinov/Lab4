#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print(*re.findall(r'.{2}(.)', input()), sep='\n')
