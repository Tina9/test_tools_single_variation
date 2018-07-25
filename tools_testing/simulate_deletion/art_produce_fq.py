#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

try:
    from config import art, machine
except:
    art = "/Users/xu/software/art_bin_MountRainier/art_illumina"
    machine = "HS25"

import subprocess

def produce_fq(raw_fasta, reads_length, multiple_count, output):

    cmd = "%s -na -p -ss %s -i %s -l %s -c %s -m 300 -s 70 -o %s" % (art, machine, raw_fasta, reads_length, multiple_count, output)
    subprocess.call(cmd, shell=True)    
    
