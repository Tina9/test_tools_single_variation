import sys
sys.path.append("../tools_testing/simulate_insertion/")
from insertion_bp import insertion_bp

bp = 10
raw_fasta = "/Users/xu/data/5.2_single_simulated_data/tests/data/raw_insertion_1.fa"

def test_insertion_bp():
    
    info_record = insertion_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":
    
    test_insertion_bp()


