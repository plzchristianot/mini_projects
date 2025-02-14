#One list of integers given and a target, take 2 numbers of that list and sum them, the result should be equal to the target

def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i,j]