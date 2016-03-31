#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start ...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('Child process %s , Father process %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a chlid process %s' % (os.getpid(), pid))

