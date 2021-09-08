
def productExceptSelf(nums):
    answer = []
    p = 1
    for i in range(len(nums)):
        answer.append(p)
        p = p * nums[i]
    p = 1
    for i in range(len(nums)-1, 0 -1, -1):
        answer[i] = answer[i] * p
        p = p * nums[i]
    return answer