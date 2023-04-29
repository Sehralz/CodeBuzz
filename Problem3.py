def missing_ele(nums):
    nums_length = len(nums)
    nums = sorted(nums)
    # print(nums,set(nums),list(set(nums)))
    full_set = set(range(0, nums[nums_length-1]))
    # print(full_set)
    missing_set = list(full_set - set(nums))
    # print(missing_set)
    missing_elements = sorted(missing_set)
    return (missing_elements)


def main():
    nums = [10, 3, 5, 7, 1]
    res = missing_ele(nums)
    print(f"Missing elements: {res}")


if __name__ == '__main__':
    main()
