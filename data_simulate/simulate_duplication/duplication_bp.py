#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import random

def raw_seq(raw_fasta):

    with open(raw_fasta, 'r') as fr:
        fr.readline()
        info = fr.readline()

    return info

def duplicated_seq(raw_base, copy_number):

    copy_number = int(copy_number)
    new_base = ''
    for i in range(copy_number):
        new_base += raw_base

    return new_base


def duplication_bp(bp, raw_fasta, copy_number):

    bp = int(bp)
    info = raw_seq(raw_fasta)

    ###### write the duplicated bases to the new fasta ######
    new_fasta = "./data/duplicated_" + str(bp) + "bp.fasta"
    ref = ">duplication_" + str(bp) + "bp.ref" + "\n"
    pos_bp = random.randint(0, 40000)
    raw_base = info[(pos_bp-1):(pos_bp-1+bp)]
    new_base = duplicated_seq(raw_base, copy_number)

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
