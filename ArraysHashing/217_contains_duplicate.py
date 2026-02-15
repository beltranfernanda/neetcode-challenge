from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1. Define a set
        2. Create a for loop
        3. Ask if the set array has each number
        4. If true return true if not return false
        5. Time complexity is O(n) and space complexity is O(n)
        """
        seen = set()
        counter = 0
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
def run_tests():
    s = Solution()

    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([], False),
        ([1], False),
        ([1, 1, 1, 1], True),
    ]

    for nums, expected in test_cases:
        result = s.containsDuplicate(nums)
        print(f"Input: {nums} | Expected: {expected} | Got: {result}")
        assert result == expected

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_tests()