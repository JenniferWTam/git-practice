# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    number = input('Enter a number to do summary. Enter 0 to exit. ')
    while number != 0 and sum < 1000:
        sum += number
        number = input('Enter a number to do summary. Enter 0 to exit. ')
    return sum
        


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
