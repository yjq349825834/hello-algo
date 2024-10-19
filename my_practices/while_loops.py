def while_loop_ii(n: int) -> int:
    """while loop (two updates)"""
    res = 0
    i = 1  # Initialize condition variable
    # Loop sum 1, 4, 10, ...
    while i <= n:
        res += i
        # Update condition variable
        i += 1
        i *= 2
    return res

if __name__ == "__main__":
    print(while_loop_ii(10))

