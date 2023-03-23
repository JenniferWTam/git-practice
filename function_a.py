def most_common_value(number_list):
    """ returns the most common element of the list
    """
    counter = 0
    num = nums[0]

    for i in nums:
        frequency = nums.count(i)
        if (frequency > counter):
            num = i
    return num


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")


print(most_common_value(nums))