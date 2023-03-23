def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number
    print(largest_number)

    # ordered_list = sorted(numbers)
    # return ordered_list[-1]
    'Jen is goint to receive an Git Push Error! ;-P'
    numbers.sort()
    return numbers[-1]


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))