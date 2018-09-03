import sys
sys.path.append("../data_simulate/simulate_duplication/")
from duplication_bp import duplication_bp

bp = 10
raw_fasta = "./data/simulate_data.fa" 

def test_duplication_bp():
    
    info_record = duplication_bp(bp, raw_fasta, 2)
    print(info_record)


if __name__ == "__main__":

    test_duplication_bp()
