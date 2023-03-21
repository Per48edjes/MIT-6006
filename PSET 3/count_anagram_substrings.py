def count_anagram_substrings(T, S):
    """
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    """
    A, H, k = [], {}, len(S[0])

    # O(|T|)
    T_prime = [ord(c) - ord("a") for c in T]
    freq = 26 * [0]
    for i in range(k):
        freq[T_prime[i]] += 1
    H[tuple(freq)] = 1
    beg, end = 0, k - 1
    while True:
        freq[T_prime[beg]] -= 1
        beg += 1
        end += 1
        if end < len(T_prime):
            freq[T_prime[end]] += 1
            hash_key = tuple(freq)
            H[hash_key] = H[hash_key] + 1 if hash_key in H else 1
        else:
            break

    # O(nk)
    for s in S:
        freq = 26 * [0]
        s_enc = [ord(c) - ord("a") for c in s]
        for i in range(k):
            freq[s_enc[i]] += 1
        hash_key = tuple(freq)
        A.append(H.get(hash_key, 0))

    return tuple(A)
