# data_simulate

A command-line toolkit to simulate illumina data for testing tools from NGS data dealing.

Please refer to [data_simulate](https://tina9.github.io/test_tools_single_variation/) for details.

## Features

- Easy to install and use
- Support for multi-threaded processing tasks
- Simulate multiple variated data at the same time

## Usuage

Please use the command line as follows to refer usuage:

./bin/main_process.py -h

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

## Contact

It will be helpful for all users to post questions on github if you have.


If the toolkit can help you save time, please click on the "Star" button on top of this page to encourage me develop more useful tools.



