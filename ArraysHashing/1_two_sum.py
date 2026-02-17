from typing import List

class Solution:
    """
    Docstring for Solution
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        expected = 0

        for index, num in enumerate(nums):
            expected = target - num

            if expected in nums_map:
                return [nums_map[expected], index]
            else:
                nums_map[num]=index
        return []
    
def run_tests():
    solution = Solution()

    test_cases = [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1]),
        ([1,2,3], 7, []),
        ([1], 2, []),
    ]

    for nums,target, expected in test_cases:
        result = solution.twoSum(nums, target)
        print(f"Inputs: {(nums, target)} | Expected: {expected} | Got: {result}")
        assert result == expected

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_tests()