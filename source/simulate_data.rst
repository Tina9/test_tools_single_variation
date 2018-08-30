.. stimulate_data documentation master file, created by
   sphinx-quickstart on Thu Aug 30 13:44:07 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=========================================
simulate_data
==========================================


Installation
============
use git to clone code::
    
    git clone git@github.com:Tina9/test_tools_single_variation.git

Usage
=====

You can type main_process.py -h for help document::

    Usage:
        main_process.py [-l=150] [-c=100000] [-b=1] [-t=1] [-p=1] [-d=4] [--dup <dup-ratio>] [--del <del-ratio>] [--ins <ins-ratio>] [--inv <inv-ratio>] [--rep <rep-ratio>]

    Testing different tools on different raw-fasta-based variations

    Options:
        -h --help
        -l,--length=150             reads length of simulated fasta [default: 150]
        -c,--count=100000           number of reads/read pairs [default: 100000]
        -b,--basepair=1             the length of variated bases [default: 1]
        -p,--copys=1                the copy number variation of duplication [default: 1]
        -t,--times=1                the repeat time [default: 1]
        -d,--thread=1               the worker threads [default: 4]
        --dup <dup-ratio>           the proportion of duplicated-variation reads in all reads
        --del <del-ratio>           the propertion of deleted-variation reads in all reads
        --ins <ins-ratio>           the propertion of inserted-variation reads in all reads
        --inv <inv-ratio>           the propertion of inversed-variation reads in all reads
        --rep <rep-ratio>           the propertion of repeated-variation reads in all reads

An example is as follows::
    
    py bin/main_process.py --dup 0.2

Contents
=========

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
