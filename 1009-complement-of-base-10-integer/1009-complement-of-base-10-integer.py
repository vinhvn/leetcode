class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        num_bits = 0
        num = n
        while num > 0:
            num_bits += 1
            num = num >> 1
        # num ^ complement = all_bits_set
        # num ^ num ^ complement = num ^ all_bits_set
        # 0 ^ complement = num ^ all_bits_set
        # complement = num ^ all_bits_set
        all_bits_set = (2 ** num_bits) - 1
        return n ^ all_bits_set
