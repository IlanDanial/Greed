# Programming Assignment 2: Greedy Algorithms

## Team
- Grecia Ocando — UFID: 34457048  
- Ilan Danial — UFID: 51879329

## Project Description
Implements and compares three cache eviction policies on the same request sequence:

- **FIFO** — First-In, First-Out
- **LRU** — Least Recently Used
- **OPTFF** — Belady's Farthest-in-Future

## Repository Structure
```
- src/cache_sim.py      # Main() function
- src/fifo.py           # FIFO eviction policy
- src/lru.py            # LRU eviction policy
- src/optff.py          # OPTFF (Belady's) eviction policy
- data/example.in       # Example input file
- data/example.out      # Expected output for example.in
- tests/test_cache.py   # Unit tests
- README.md             # Descrition of Project
```

## How to Build / Compile
No build is required, the project is built with Python.

**Dependencies:** Python 3.6+ (Recommended: 3.11.8)

## How to Run
From the project root directory:

```bash
python src/cache_sim.py <input_file>
```

### Example
```bash
python src/cache_sim.py data/example.in
```

**Expected output** (also in `data/example.out`):
```
FIFO  : 9
LRU   : 10
OPTFF : 7
```

## How to Run Tests
```bash
python tests/test_cache.py
```

## Input Format
The input file must contain exactly two lines:
```
k m
r1 r2 r3 ... rm
```
- `k` — cache capacity
- `m` — number of requests
- `r1 .. rm` — space-separated integer request IDs

## Output Format
```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## Assumptions
- Input is well-formed and follows the format described above.
- Request IDs are integers.
- Cache capacity `k` is at least 1.
- The program reads input from a file path passed as a command-line argument.

## Written Component

### How each eviction policy works:

**FIFO:**  Has a queue with items kept in the order they were inserted. When there is a cache miss with the cache being full,the earliest item is thrown out.

**LRU:** Keeps track of the most recent use of each cached item. When there is a cache miss with the cache being full, the item that was accessed farthest in the past is evicted. When a hit happens that item is updated to be the most recently used.

**OPTFF (Belady's Algorithm):** When there is a cache miss with the cache being full, looks forward in the remaining request sequence and evicts the item whose next access is farthest in the future. If an item is does not get accessed again, it is evicted right away.