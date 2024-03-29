class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = list(num1)
        nums2 = list(num2)
        carry = 0
        res = []

        while nums1 or nums2:
            n1 = n2 = 0
            if nums1:
                n1 = ord(nums1.pop()) - ord("0")
            if nums2:
                n2 = ord(nums2.pop()) - ord("0")
            carry, remainder = divmod(n1 + n2 + carry, 10)
            res.append(str(remainder))
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])
