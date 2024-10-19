def for_loop(n: int) -> int:
    """for loop"""
    res = 0
    # Loop sum 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        res += i
    return res


if __name__== "__main__":
    print(for_loop(10))