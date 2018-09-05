#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import sys
import os
from docopt import docopt
import concurrent.futures
dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../data_simulate")
sys.path.insert(0, dirpath)
from simulate_duplication.simulate_duplication import main_duplication
from simulate_deletion.simulate_deletion import main_deletion
from simulate_insertion.simulate_insertion import main_insertion
from simulate_inversion.simulate_inversion import main_inversion
from simulate_replacement.simulate_replacement import main_replacement

def call_functions(arguments):

    reads_length = arguments['--length']
    reads_count = arguments['--count']
    bp = arguments['--basepair']
    repeat_time = arguments['--times']
    copy_number = arguments['--copys']

    sum_info = []

    if arguments['--dup']:
        dup_ratio = arguments['--dup']
        dup_multiple_count = int(reads_count) * (1 - float(dup_ratio))
        dup_single_count = int(reads_count) * float(dup_ratio)
        dup_info_reocrd, dup_sum_info = main_duplication(reads_length, dup_multiple_count, dup_single_count, bp, repeat_time, copy_number)

        sum_info.append(dup_info_reocrd)

    if arguments['--del']:
        del_ratio = arguments['--del']
        del_multiple_count = int(reads_count) * (1 - float(del_ratio))
        del_single_count = int(reads_count) * float(del_ratio)
        del_info_record, del_sum_info = main_deletion(reads_length, del_multiple_count, del_single_count, bp, repeat_time)

        sum_info.append(del_info_record)

    if arguments['--ins']:
        ins_ratio = arguments['--ins']
        ins_multiple_count = int(reads_count) * (1 - float(ins_ratio))
        ins_single_count = int(reads_count) * float(ins_ratio)
        ins_info_record, ins_sum_info = main_insertion(reads_length, ins_multiple_count, ins_single_count, bp, repeat_time)

        sum_info.append(ins_info_record)

    if arguments['--inv']:
        inv_ratio = arguments['--inv']
        inv_multiple_count = int(reads_count) * (1 - float(inv_ratio))
        inv_single_count = int(reads_count) * float(inv_ratio)
        inv_info_record, inv_sum_info = main_inversion(reads_length, inv_multiple_count, inv_single_count, bp, repeat_time)

        sum_info.append(inv_info_record)

    if arguments['--rep']:
        rep_ratio = arguments['--rep']
        rep_multiple_count = int(reads_count) * (1 - float(rep_ratio))
        rep_single_count = int(reads_count) * float(rep_ratio)
        rep_info_record, rep_sum_info = main_replacement(reads_length, rep_multiple_count, rep_single_count, bp, repeat_time)

        sum_info.append(rep_info_record)

    return sum_info


def main_function(arguments):
    
    sum_info = call_functions(arguments)

    return sum_info

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
        -d,--thread=1               the worker threads [default: 1]
        --dup <dup-ratio>           the proportion of duplicated-variation reads in all reads
        --del <del-ratio>           the propertion of deleted-variation reads in all reads
        --ins <ins-ratio>           the propertion of inserted-variation reads in all reads
        --inv <inv-ratio>           the propertion of inversed-variation reads in all reads
        --rep <rep-ratio>           the propertion of repeated-variation reads in all reads
    """

    arguments = docopt(usage)

    worker_num = int(arguments['--thread'])
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=worker_num)
    future = executor.submit(main_function, arguments)

