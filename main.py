from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if num + num2 == target:
                return [i,j+i+1]

