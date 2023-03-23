def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    'Jen is goint to receive an Git Push Error! ;-P'
    ordered_list = sorted(numbers)
    return ordered_list[-1]


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))