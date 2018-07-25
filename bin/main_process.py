#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import sys
import os
from docopt import docopt

def main_function():
    pass

if __name__ == "__main__":
    usage = """
    Usage:
        main_process.py 

    Testing different tools using simulated data

    Arguments:

    Options:

    """

    arguments = docopt(usage)
    main_function()
