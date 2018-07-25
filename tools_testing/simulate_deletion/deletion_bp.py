#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "zhangxu"

import random

def raw_seq(raw_fasta):

    with open(raw_fasta, 'r') as fr:
        fr.readline()
        info = fr.readline()
        
    return info

def deletion_bp(bp, raw_fasta):

    info = raw_seq(raw_fasta)

    ###### write the deleted bases to the new fasta ######
    new_fasta = "./data/deletion_" + str(bp) + "bp.fasta"
    ref = ">del_" + str(bp) + "bp.ref" + "\n"
    pos_bp = random.randint(0, 40000)
    raw_base = info[pos_bp : (pos_bp + int(bp))]
    new_info = info[:(pos_bp - 1)] + info[(pos_bp + int(bp)):]
    with open(new_fasta, 'w') as fr:
        fr.write(ref)
        fr.write(new_info)

    ###### use the dictionary to save the variated information ######
    info_record = {}
    var_interval = str(pos_bp) + "-" + str(pos_bp + int(bp))
    var_type = str(bp) + "bp"
    info_record["info"] = [var_type, var_interval, raw_base]
    info_record["fasta"] = new_fasta

    return info_record

    
