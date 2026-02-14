from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. Inputs : 2 strings can have different length
        2. Output : boolean; True if same length and letters otherwise false
        
        My solution
        1. If different length then return false
        2. Convert one str to set to map each letter
        3. Compare for each letter in the inputs if the count is the same
        4. If not return false otherwise return true
        """
        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False

        return True
    
def run_tests():
    solution = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
    ]

    for s,t, expected in test_cases:
        result = solution.isAnagram(s, t)
        print(f"Inputs: {(s,t)} | Expected: {expected} | Got: {result}")
        assert result == expected

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_tests()