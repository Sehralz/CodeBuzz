def repeated_val(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    repeated_nums = [num for num in count_dict if count_dict[num] > 1]
    print(count_dict)
    print(f"Repeated Values: {repeated_nums}")


def main():
    nums = [2, 4, 5, 0, 7, 2, 4, 9, 0, 1]
    repeated_val(nums)


if __name__ == '__main__':
    main()
