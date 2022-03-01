#!/usr/bin/env python3

import random


def gen_hexstring(size=16):
    string = ''.join([
        random.choice('0123456789abcdef')
        for _ in range(size)
    ])
    return string
