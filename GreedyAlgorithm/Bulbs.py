"""
    Problem: Given N bulbs, either 1 or 0.
        Turning ON ith bulb causing all remaining bulbs to flip.
        E.g. initial array of bulbs: [1, 0, 1, 0]
        switching ON 2nd bulb (at index 1) to 1 will cause 3rd bulb to flip to 0 and 4th bulb to flip to 1
        resulting array would be [1, 1, 0, 1]

        Find the minimum number of switches to turn all the bulbs ON.

    Constraint:
        1. 1 <= N <= 10^5
        2. A[i] = {0, 1}
"""
from typing import List


def toggle(bit: int) -> int:
    """
    Toggle 1 to 0 and 0 to 1
    Ideally I should use a boolean variable to do that but just for the sake of similarity with the given problem
    :param bit:
    :return:
    """
    # Using XOR operation
    # for bit = 0, 1 XOR 0 = 1
    # for bit = 1, 1 XOR 1 = 0
    return 1 ^ bit


def max_switch(bulbs: List[int]) -> int:
    """
    Naive approach: for each element in the array, flip all remaining elements until you reach last element
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param bulbs:
    :return:
    """
    n = len(bulbs)
    count = 0
    for i in range(n):
        if bulbs[i] == 0:
            count += 1
            for j in range(i, n):
                bulbs[j] = toggle(bulbs[j])
    return count


def max_switch_opt(bits: List[int]) -> int:
    """
    Better approach: in each iteration, do not iterate rest of the bits to actually flip it.
        We can leverage the fact that, flipping even times would make it again as original,
        and odd times make it opposite.
        We can keep track of this fact, and store another bit let's say flip_bit
        with each flipping, we will flip the flip_bit
        and for each element, will take it's original value and flip_bit to decide what would be the actual value
        if we would have actually flipped each bit.
    Time Complexity: O(n)
    Space Complexity:
    :param bits:
    :return:
    """
    n = len(bits)
    count = 0
    for i in range(n):
        """ 
        XOR operation between current bit and flip bit give the final bit status -- Below truth table
            +----------------------------------+            
            |  flip_bit | current_bit | result |
            +-----------+-------------+--------+
            |     0     |      0      |   0    | --> flip_bit is 0 so no need to change the original bit
            |     0     |      1      |   1    | --> flip_bit is 0 so no need to change the original bit
            |     1     |      0      |   1    | --> flip_bit is 1 so change the original bit from 0 to 1
            |     1     |      1      |   0    | --> flip_bit is 1 so change the original bit from 1 to 0
            +-----------+-------------+--------+
        """
        flip_bit = count % 2  # 0 for even, 1 for odd
        if bits[i] ^ flip_bit == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(f"Greedy Algorithm: Bulb Flip Problem")
    print(f"max_switch([1, 0, 1]) = {max_switch([1, 0, 1])}, Expected = 2")
    print(f"max_switch([0, 1, 0, 1, 1, 0, 1, 1]) = {max_switch([0, 1, 0, 1, 1, 0, 1, 1])}, Expected = 6")
    print(f"max_switch_opt([1, 0, 1]) = {max_switch_opt([1, 0, 1])}, Expected = 2")
    print(f"max_switch_opt([0, 1, 0, 1, 1, 0, 1, 1]) = {max_switch_opt([0, 1, 0, 1, 1, 0, 1, 1])}, Expected = 6")
