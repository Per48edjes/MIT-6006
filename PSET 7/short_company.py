from functools import cache


# NOTE: We're cheating a little bit with the builtin `cache` decorator and
#       keeping intermediate lists rather than recovering parent pointers.
def short_company(C, P, n, k):
    """
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of
              | decreasing prices from c that doesn't skip days
    """

    @cache
    def shorting_path_at_i(company_idx: int, price_idx: int) -> list[int]:
        max_shorting_path = []
        max_shorting_value = float("-inf")
        for j in range(
            price_idx,
            ((price_idx // k) + 1) * k + (k - 1) + 1,
        ):
            if j >= n * k:
                break
            if P[company_idx][price_idx] > P[company_idx][j]:
                path = shorting_path_at_i(company_idx, j)
                if len(path) > max_shorting_value:
                    max_shorting_path = path
                    max_shorting_value = len(path)
        return [P[company_idx][price_idx]] + max_shorting_path

    best_company = ""
    best_company_path = []
    for c, company_name in enumerate(C):
        for i in range(n * k):
            path = shorting_path_at_i(c, i)
            if len(path) > len(best_company_path):
                best_company_path = path
                best_company = company_name

    return (best_company, best_company_path)
