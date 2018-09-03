import sys
sys.path.append("../data_simulate/simulate_replacement/")
from replacement_bp import replacement_bp

bp = 10
raw_fasta = "./data/simulate_data.fa"

def test_replacement_bp():
    
    info_record = replacement_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":

    test_replacement_bp()
