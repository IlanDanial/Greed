import sys
from fifo import fifo
from lru import lru
from optff import optff


def main():
    if len(sys.argv) < 2:
        print("Usage: python cache_sim.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        first_line = f.readline().split()
        k = int(first_line[0])
        m = int(first_line[1])
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru(k, requests)
    optff_misses = optff(k, requests)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")


if __name__ == "__main__":
    main()
