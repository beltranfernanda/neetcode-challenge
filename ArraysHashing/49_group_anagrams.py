from collections import defaultdict
from typing import List

class Solution:
    def groupAnagramsBruteForce(self, strs: List[str]) -> List[List[str]]:
        """
         1. Function to evaluate if 2 strings are anagrams
         2. Function to group each subgroup of anagrams
         3. If no pair is found for a word then it is allocate it in a single array
         4. If input is empty or only posess 1 word then a formatted bidimensional
         array is returned -> Edge case
         5. Create a set to map indexes of already grouped words to avoid repeating 
         in brute force solution
         6. Loops complexity O(n^2) + O(k log k) so O(n^2 * k log k)
         7. K is length per words and n words
        """
        result = []
        strsLen = len(strs)

        if strsLen == 1:
            return [[strs[0]]]

        visited = set()

        for i in range(strsLen):
            if i in visited:
                continue

            templist = [strs[i]]
            visited.add(i)

            for j in range(i + 1, strsLen):
                if self.isAnagramBruteForce(strs[i], strs[j]):
                    templist.append(strs[j])
                    visited.add(j)

            result.append(templist)

        return result

    def isAnagramBruteForce(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        for letter in set(s1):
            if s1.count(letter) != s2.count(letter):
                return False

        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams
        anagram_map = defaultdict(list)
        for word in strs:
            # Sort letters of the word to create a canonical key
            sorted_key = "".join(sorted(word))
            anagram_map[sorted_key].append(word)

        # Return all grouped anagrams as a list of lists
        return list(anagram_map.values())


def run_tests():
    solution = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ]

    for strs, expected in test_cases:
        result = solution.groupAnagrams(strs)
        print(f"Input: {(strs)} | Expected: {expected} | Got: {result}")
        assert result == expected

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_tests()
