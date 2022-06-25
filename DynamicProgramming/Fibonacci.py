from typing import Dict


def fib_rec(n: int) -> int:  #
    """
    Finds nth fibonacci number - Recursive solution
    Time Complexity = O(2^n)
    Space Complexity = O(n)
    :param n:
    :return:
    """
    if n < 1:
        print(f"Error: Invalid input")
        return 0
    if n <= 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dp(n: int, memo: Dict[int, int] = {0: 0, 1: 1, 2: 1}) -> int:
    """
    Finds nth fibonacci number - Recursive solution with Dynamic Programming technique using memoization
    Time Complexity = O(n)
    Space Complexity = O(n)
    :param memo: A map to store already computed results
    :param n:
    :return:
    """
    if n not in memo:
        memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


def fib(n: int) -> int:
    """
    Finds nth fibonacci number - Iterative solution
    Time Complexity = O(n)
    Space Complexity = O(1)
    :param n:
    :return:
    """
    if n < 1:
        print(f"Error: Invalid input")
        return 0
    if n <= 2:
        return 1
    last = 1
    second_last = 1
    for i in range(n - 2):
        current = last + second_last
        second_last = last
        last = current
    return current


if __name__ == '__main__':
    # Iterative
    print(f"fib(5) = {fib(5)}")
    print(f"fib(7) = {fib(7)}")
    print(f"fib(10) = {fib(10)}")
    print(f"fib(35) = {fib(35)}")
    print(f"fib(100) = {fib(100)}")

    # Recursive
    print(f"fib(5) = {fib_rec(5)}")
    print(f"fib(7) = {fib_rec(7)}")
    print(f"fib(10) = {fib_rec(10)}")
    print(f"fib_dp(50) = {fib_dp(50)}")
    print(f"fib(35) = {fib_rec(35)}")
    # print(f"fib(50) = {fib(50)}")
