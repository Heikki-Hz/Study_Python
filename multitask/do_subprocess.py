#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('$ ping www.python.org')
r = subprocess.call(['ping', 'www.python.org'])
print('Exit code:', r)
