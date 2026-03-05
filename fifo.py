from collections import deque


def fifo(k, requests):
    cache = set()
    queue = deque()
    misses = 0

    for r in requests:
        if r in cache:
            continue
        misses += 1
        if len(cache) < k:
            cache.add(r)
            queue.append(r)
        else:
            evicted = queue.popleft()
            cache.remove(evicted)
            cache.add(r)
            queue.append(r)

    return misses
