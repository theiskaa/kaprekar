#
# Kaprekar's constant (6174) is a mathematical curiosity in number theory.
# When you take any four-digit number (with at least two different digits),
# arrange its digits in descending and ascending order to form two numbers,
# subtract the smaller from the larger, and repeat this process, you'll
# always reach 6174 in at most 7 steps. Once you reach 6174, the process
# will cycle: 7641-1467=6174, and so on.
#

import random

KAPREKAR_CONSTANT = 6174


def get_random_four_digit():
    return random.randint(1000, 9999)


def kaprekar_step(number):
    digits = list(str(number))
    digits.sort()
    min_num = int(''.join(digits))
    max_num = int(''.join(digits[::-1]))
    return max_num - min_num


def kaprekar_loop(number):
    steps = 1
    current = number
    print(f"step::{steps}: {current}")

    while current != KAPREKAR_CONSTANT:
        digits = list(str(current))
        digits.sort()
        min_num = int(''.join(digits))
        max_num = int(''.join(digits[::-1]))
        result = max_num - min_num
        steps += 1
        print(f"step::{steps}: {max_num} - {min_num} = {result}")
        current = result

    print(
        f"> Reached Kaprekar's constant `{KAPREKAR_CONSTANT}` in `{steps}` steps!")
    return steps


if __name__ == "__main__":
    number = get_random_four_digit()
    print(f"Starting number: {number}")
    kaprekar_loop(number)
