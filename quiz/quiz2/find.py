def find_max(nums, biggest_num=None):
    if len(nums) == 0:
        return biggest_num
    if biggest_num is None or nums[0] > biggest_num:
        biggest_num = nums[0]

    return find_max(nums[1:], biggest_num)
