def arrayPartition(nums):
    return sum(sorted(nums)[::2])

print(arrayPartition([1,4,3,2]))