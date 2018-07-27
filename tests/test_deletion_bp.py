import sys
sys.path.append("../tools_testing/simulate_deletion")
from deletion_bp import deletion_bp

raw_fasta = "./data/raw_deletion_10.fa"
bp = 10

def test_deletion_bp():

    info_record = deletion_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":

    test_deletion_bp()
