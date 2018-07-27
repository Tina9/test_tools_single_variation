#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import random

def raw_seq(raw_fasta):

    with open(raw_fasta, 'r') as fr:
        fr.readline()
        info = fr.readline()

    return info

def random_seq(bp):
    seq_container = ['A', 'T', 'C', 'G']
    seq = ""
    for i in range(bp):
        seq += random.choice(seq_container)

    return seq

def replacement_bp(bp, raw_fasta):

    bp = int(bp)
    info = raw_seq(raw_fasta)

    ###### write the replaced bases to the new fasta ######
    new_fasta = "./data/replacement_" + str(bp) + "bp.fasta"
    ref = ">replace_" + str(bp) + "bp.ref" + "\n"
    pos_bp = random.randint(0, 40000)
    raw_base = info[(pos_bp-1):(pos_bp-1+bp)]
    new_base = random_seq(bp)

    while raw_base == new_base:
        new_base = random_seq(bp)

    new_info = info[:(pos_bp-1)] + new_base + info[(pos_bp-1+bp):]
    with open(new_fasta, 'w') as fw:
        fw.write(ref)
        fw.write(new_info)

    ###### use the dictionary to save the variated information ######
    info_record = {}
    var_interval = str(pos_bp) + "-" + str(pos_bp + bp)
    var_type = str(bp) + "bp"
    info_record['info'] = [var_type, var_interval, raw_base, new_base]
    info_record['fasta'] = new_fasta

    return info_record
