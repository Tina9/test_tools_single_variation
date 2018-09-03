import sys
sys.path.append("../data_simulate/simulate_inversion/")
from inversion_bp import inversion_bp

bp = 10
raw_fasta = "./data/simulate_data.fa"

def test_inversion_bp():
    
    info_record = inversion_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":

    test_inversion_bp()
