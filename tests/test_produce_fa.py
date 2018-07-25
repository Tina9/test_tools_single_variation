import sys
sys.path.append("../tools_testing/simulate_deletion/")
from produce_fa import produce_fasta

test = "simulate_data"

def test_produce_fasta():

    fasta_name = produce_fasta(test)
    print(fasta_name)

if __name__ == "__main__":

    test_produce_fasta()    
