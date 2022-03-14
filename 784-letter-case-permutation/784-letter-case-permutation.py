class Solution:
    def letterCasePermutation(self, string: str) -> List[str]:
        permutations = [""]
        for char in string:
            # take all existing permutations and add current character to create new ones
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.pop(0)
                # if character is numeric, simply add it and continue
                if not char.isalpha():
                    permutations.append(oldPermutation + char)
                    continue
                # if character is alphabetical, add both lowercase and uppercase
                permutations.append(oldPermutation + char.lower())
                permutations.append(oldPermutation + char.upper())

        return permutations
