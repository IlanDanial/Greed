from collections import OrderedDict


def lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for r in requests:
        if r in cache:
            cache.move_to_end(r)
            continue
        misses += 1
        if len(cache) < k:
            cache[r] = True
        else:
            cache.popitem(last=False)
            cache[r] = True

    return misses
