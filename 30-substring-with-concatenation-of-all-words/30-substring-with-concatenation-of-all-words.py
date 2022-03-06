class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        matches = 0
        indices = []
        num_word = len(words)
        len_word = len(words[0])
        for i in range(len(s) - (len_word * num_word) + 1):
            curr_freq = {}
            for j in range(num_word):
                idx_start = i + j * len_word
                idx_end = idx_start + len_word
                word = s[idx_start:idx_end]

                if word not in word_freq:
                    break

                curr_freq[word] = curr_freq.get(word, 0) + 1
                if curr_freq[word] > word_freq[word]:
                    break

                if j == num_word - 1:
                    indices.append(i)
        return indices
