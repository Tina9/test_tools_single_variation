#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import sys
import os
from docopt import docopt
dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../tools_testing")
sys.path.insert(0, dirpath)
from simulate_duplication.simulate_duplication import main_duplication
from simulate_deletion.simulate_deletion import main_deletion
from simulate_insertion.simulate_insertion import main_insertion
from simulate_inversion.simulate_inversion import main_inversion
from simulate_replacement.simulate_replacement import main_replacement

def call_functions(arguments):

    reads_length = arguments['--length']
    del_multiple_count = int(arguments['--count']) * (1 - float(arguments['DEL']))
    del_single_count = int(arguments['--count']) * float(arguments['DEL'])
    ins_multiple_count = int(arguments['--count']) * (1 - float(arguments['INS']))
    ins_single_count = int(arguments['--count']) * float(arguments['INS'])
    inv_multiple_count = int(arguments['--count']) * (1 - float(arguments['INV']))
    inv_single_count = int(arguments['--count']) * float(arguments['INV'])
    rep_multiple_count = int(arguments['--count']) * (1 - float(arguments['REP']))
    rep_single_count = int(arguments['--count']) * float(arguments['REP'])
    dup_multiple_count = int(arguments['--count']) * (1 - float(arguments['DUP']))
    dup_single_count = int(arguments['--count']) * float(arguments['DUP'])
    bp = arguments['--basepair']
    repeat_time = arguments['--times']
    copy_number = arguments['--copys']
    max_worker = arguments['--thread']

    main_deletion(reads_length, del_multiple_count, del_single_count, bp, repeat_time)


def main_function(arguments):
    
    call_functions(arguments)

if __name__ == "__main__":
    usage = """
    Usage:
        main_process.py [-l=150] [-c=100000] [-b=1] [-t=1] [-p=1] [-d=1] DUP DEL INS INV REP

    Testing different tools on different raw-fasta-based variations

    Arguments:
        DUP         the proportion of duplicated-variation fastas in all fastas
        DEL         the proportion of deleted-variation fastas in all fastas
        INS         the proportion of inserted-variation fastas in all fastas
        INV         the proportion of inversed-variation fastas in all fastas
        REP         the proportion of replaced-variation fastas in all fastas

    Options:
        -h --help
        -l,--length=150         reads length of simulated fasta [default: 150]
        -c,--count=100000       number of reads/read pairs [default: 100000]
        -b,--basepair=1         the length of variated bases [default: 1]
        -p,--copys=1            the copy number variation of duplication [default: 1]
        -t,--times=1            the repeat time [default: 1]
        -d,--thread=1          the worker threads
    """

    arguments = docopt(usage)
    main_function(arguments)

    """

    arguments = docopt(usage)
    main_function()
