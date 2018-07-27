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
    bp = arguments['--count']
    repeat_time = arguments['--times']
    copy_number = arguments['--copys']
    max_worker = arguments['--thread']

    if arguments['--dup']:
        dup_ratio = arguments['--dup']
        dup_multiple_count = int(dup_ratio) * (1 - float(dup_ratio))
        dup_single_count = int(dup_ratio) * float(dup_ratio)
        main_deletion(reads_length, del_multiple_count, del_single_count, bp, repeat_time)

    if arguments['--del']:
        del_ratio = arguments['--del']

    if arguments['--ins']:
        ins_ratio = arguments['--ins']

    if arguments['--inv']:
        inv_ratio = arguments['--inv']

    if arguments['--rep']:
        rep_ratio = arguments['--rep']

def main_function(arguments):
    
    call_functions(arguments)

if __name__ == "__main__":
    usage = """
    Usage:
        main_process.py [-l=150] [-c=100000] [-b=1] [-t=1] [-p=1] [-d=1] [--dup <dup-ratio>] [--del <del-ratio>] [--ins <ins-ratio>] [--inv <inv-ratio>] [--rep <rep-ratio>]

    Testing different tools on different raw-fasta-based variations

    Options:
        -h --help
        -l,--length=150             reads length of simulated fasta [default: 150]
        -c,--count=100000           number of reads/read pairs [default: 100000]
        -b,--basepair=1             the length of variated bases [default: 1]
        -p,--copys=1                the copy number variation of duplication [default: 1]
        -t,--times=1                the repeat time [default: 1]
        -d,--thread=1               the worker threads
        --dup <dup-ratio>           the proportion of duplicated-variation reads in all reads
        --del <del-ratio>           the propertion of deleted-variation reads in all reads
        --ins <ins-ratio>           the propertion of inserted-variation reads in all reads
        --inv <inv-ratio>           the propertion of inversed-variation reads in all reads
        --rep <rep-ratio>           the propertion of repeated-variation reads in all reads
    """

    arguments = docopt(usage)
    main_function(arguments)

