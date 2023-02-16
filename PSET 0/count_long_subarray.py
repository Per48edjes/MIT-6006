def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count, len_lsa = 1, 0
    beg, end, len_sa = 0, 1, 1
    while end < len(A):
        if A[end] > A[beg]:
            len_sa += 1
            beg += 1
        else:
            if len_sa > len_lsa:
                len_lsa, count = len_sa, 1
            elif len_sa == len_lsa:
                count += 1
            beg, len_sa = end, 1
        end += 1
    else:
        if len_sa > len_lsa:
            count = 1
        elif len_sa == len_lsa:
            count += 1
    return count
