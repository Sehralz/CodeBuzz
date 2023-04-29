def sort_array(nums):
    """
    Sort an Array with elemenst as 0s, 1s, and 2s 
    Dutch National Flag Algorithm
    """
    low, mid, high = 0, 0, (len(nums)-1)
    #print(len(nums),low,mid,high)
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


def main():
    nums = [1,2,0,1,1,0,2,0,2,2] 
    nums = sort_array(nums)
    print(f"Final array be: {nums}")

if __name__ == '__main__':
    main()
