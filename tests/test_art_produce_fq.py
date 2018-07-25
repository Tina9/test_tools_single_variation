import sys
sys.path.append("../tools_testing/simulate_deletion")
from art_produce_fq import produce_fq

raw_fasta = "./data/simulate_data.fa"
reads_length = 150
multiple_count = 100000
multi_output = "./data/multiple"
single_output = "./data/single"

def test_multiple_fq():
    
    produce_fq(raw_fasta, reads_length, multiple_count, multi_output)
    produce_fq(raw_fasta, reads_length, multiple_count, single_output)

if __name__ == "__main__":
    
    test_multiple_fq()
