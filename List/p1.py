def twoSum(nums,target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    ##키값은 숫자, 값은 인덱스
    for i , num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
    ## target- 숫자가 nums_map에 잇고 인덱스가 중복되지 않을 때
            return[i,nums_map[target-num]]

print(twoSum([2,7,11,15],9))