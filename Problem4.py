def prod_ele(nums):
    result = []
    for num in range(len(nums)):
        product = 1
        for numitr in range(len(nums)):
            if (num != numitr):
                product = product * nums[numitr]
        result.append(product)
    print(result)


def main():
    nums = [1, 2, 3, 4, 5]
    prod_ele(nums)


if __name__ == '__main__':
    main()
