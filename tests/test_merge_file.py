import sys
sys.path.append("../tools_testing/simulate_deletion")
from merge_file import merge_file

files = ["./data/multiple_0_1bp_", "./data/single_0_1bp_"]

def test_merge_files():
    
    fq1, fq2 = merge_file(files)
    print(fq1, fq2)

if __name__ == "__main__":

    test_merge_files()
