from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        # Initialize dictionary
        for num in nums:
            frequencies[num]=0

        # Calculate frequencies
        for num in nums:
            frequencies[num]+=1

        # Order by values and return the first k values
        freqSorted = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        return list(freqSorted)[:k]
    
    def topKFrequentOptimal(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, freq in counter.most_common(k)]

        
    
def run_tests():
    solution = Solution()

    test_cases = [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
        ([1,2,1,2,1,2,3,1,3,2], 2, [1,2])
    ]

    for nums,k, expected in test_cases:
        result = solution.topKFrequentOptimal(nums, k)
        print(f"Inputs: {(nums,k)} | Expected: {expected} | Got: {result}")
        assert result == expected

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_tests()