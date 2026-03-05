import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fifo import fifo
from lru import lru
from optff import optff


def test_example():
    k = 3
    requests = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

    assert fifo(k, requests) == 9, f"FIFO expected 9, got {fifo(k, requests)}"
    assert lru(k, requests) == 10, f"LRU expected 10, got {lru(k, requests)}"
    assert optff(k, requests) == 7, f"OPTFF expected 7, got {optff(k, requests)}"
    print("All tests passed.")


def test_single_capacity():
    k = 1
    requests = [1, 2, 1, 2]

    assert fifo(k, requests) == 4
    assert lru(k, requests) == 4
    assert optff(k, requests) == 4
    print("Single capacity test passed.")


def test_all_hits():
    k = 5
    requests = [1, 2, 3, 1, 2, 3, 1, 2, 3]

    assert fifo(k, requests) == 3
    assert lru(k, requests) == 3
    assert optff(k, requests) == 3
    print("All hits test passed.")


if __name__ == "__main__":
    test_example()
    test_single_capacity()
    test_all_hits()
    print("All tests passed!")
