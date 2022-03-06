class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = {}
        highest_fruit_count = 0
        start = 0
        for end in range(len(fruits)):
            if fruits[end] not in hashmap:
                hashmap[fruits[end]] = 0
            hashmap[fruits[end]] += 1

            while len(hashmap) > 2:
                hashmap[fruits[start]] -= 1
                if hashmap[fruits[start]] == 0:
                    del hashmap[fruits[start]]
                start += 1

            highest_fruit_count = max(highest_fruit_count, end-start+1)
        return highest_fruit_count