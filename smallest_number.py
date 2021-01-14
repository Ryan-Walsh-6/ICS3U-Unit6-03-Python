#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program picks out the smallest number out of 10 random numbers

import random


def smallest_number(list_of_numbers):
    # checks smallest numb

    # process & output
    for loop_counter in (list_of_numbers):
        if list_of_numbers[0] > loop_counter:
            list_of_numbers[0] = loop_counter

    return list_of_numbers[0]


def main():
    # this program picks out the smallest number out of 10 random numbers
    my_numbers = []
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)

    for loop_counter in range(0, 10):
        print("The random number {0} is: {1}".format(loop_counter + 1,
                                                     my_numbers[loop_counter]))

    small_numb = smallest_number(my_numbers)

    print("\n", end="")
    print("The smallest number is {0}".format(small_numb))


if __name__ == "__main__":
    main()
