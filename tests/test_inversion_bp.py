import sys
sys.path.append("../tools_testing/simulate_inversion/")
from inversion_bp import inversion_bp

bp = 10
raw_fasta = "/Users/xu/data/5.2_single_simulated_data/tests/data/raw_inversion_1.fa"

def test_inversion_bp():
    
    info_record = inversion_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":

    test_inversion_bp()
