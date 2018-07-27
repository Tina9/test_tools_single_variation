#!/usr/bin/env python3
# -*- coding:utf-8 -8_

def file_sort(files):

    fastq1 = []
    fastq2 = []
    for fi in files:
        fq1 = fi + "1.fq"
        fq2 = fi + "2.fq"
        fastq1.append(fq1)
        fastq2.append(fq2)

    return fastq1, fastq2

def merge_sorting(fastq, sum_fq):

    with open(sum_fq, 'w') as fw:
        for i in fastq:
            with open(i, 'r') as fr:
                fw.write(fr.read())

def merge_file(files):

    sum_fq1 = "./data/simulate1.fq"
    sum_fq2 = "./data/simulate2.fq"

    fastq1, fastq2 = file_sort(files)

    merge_sorting(fastq1, sum_fq1)
    merge_sorting(fastq2, sum_fq2)

    return sum_fq1, sum_fq2
            
