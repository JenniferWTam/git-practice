# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    num_sum = 0
    number = int(input('Enter a number to do summary. Enter 0 to exit. '))
    while number != 0 and num_sum < 1000:
        num_sum += number
        number = int(input('Enter a number to do summary. Enter 0 to exit. '))
    return num_sum
        


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
