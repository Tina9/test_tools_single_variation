import sys
sys.path.append("../data_simulate/simulate_insertion/")
from insertion_bp import insertion_bp

bp = 10
raw_fasta = "./data/simulate_data.fa"

def test_insertion_bp():
    
    info_record = insertion_bp(bp, raw_fasta)
    print(info_record)

if __name__ == "__main__":
    
    test_insertion_bp()


