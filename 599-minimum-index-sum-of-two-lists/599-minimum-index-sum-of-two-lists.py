class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1WordIndexMap = { word: i for i, word in enumerate(list1) }
        list2WordIndexMap = { word: i for i, word in enumerate(list2) }
        
        minIndexSum = math.inf
        minIndexWords = []
        
        for word in list1WordIndexMap:
            if word in list2WordIndexMap:
                indexSum = list1WordIndexMap[word] + list2WordIndexMap[word]
                if indexSum < minIndexSum:
                    minIndexSum = indexSum
                    minIndexWords = [word]
                elif indexSum == minIndexSum:
                    minIndexWords.append(word)
        
        return minIndexWords

