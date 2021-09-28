class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_word_map = {}
        words = s.split(' ')
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False

        for i, word in enumerate(words):
            if pattern[i] in pattern_word_map:
                if pattern_word_map[pattern[i]] != word:
                    return False
            else:
                pattern_word_map[pattern[i]] = word
        return True
