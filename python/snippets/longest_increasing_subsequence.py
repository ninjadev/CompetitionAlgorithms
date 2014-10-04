def longest_increasing_subsequence(d):
    """Return one of the Longest Increasing Subsequences of list d"""

    candidates = []
    for i in range(len(d)):
        suitable_candidates = [candidates[j] for j in range(i) if candidates[j][-1] < d[i]]
        best_candidate = max(suitable_candidates or [[]], key=len)
        candidates.append(best_candidate + [d[i]])

    return max(candidates, key=len)

print longest_increasing_subsequence([3, 2, 6, 4, 5, 1])
# [3, 4, 5]

print longest_increasing_subsequence([1, 5, 2, 7, 6, 5, 2, 8, 0, 4, 5, 6, 9])
# [1, 2, 4, 5, 6, 9]
