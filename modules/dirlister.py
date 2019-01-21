#!/usr/bin/env python3

import os

def run(**args):
    print("[*] In dislister module.")
    files = os.listdir(".")

    return str(files)
