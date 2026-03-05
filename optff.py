def optff(k, requests):
    cache = set()
    misses = 0
    n = len(requests)

    for i, r in enumerate(requests):
        if r in cache:
            continue
        misses += 1
        if len(cache) < k:
            cache.add(r)
        else:
            farthest_item = None
            farthest_use = -1
            for item in cache:
                next_use = None
                for j in range(i + 1, n):
                    if requests[j] == item:
                        next_use = j
                        break
                if next_use is None:
                    farthest_item = item
                    break
                if next_use > farthest_use:
                    farthest_use = next_use
                    farthest_item = item
            cache.remove(farthest_item)
            cache.add(r)

    return misses
