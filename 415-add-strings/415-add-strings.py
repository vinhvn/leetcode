class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def getInt(n):
            return ord(n) - 48

        carry = 0
        ans = []
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 and p2 >= 0:
            s = getInt(num1[p1]) + getInt(num2[p2]) + carry
            digit = s % 10
            carry = s // 10
            ans.append(str(digit))
            p1 -= 1
            p2 -= 1
        while p1 >= 0:
            s = getInt(num1[p1]) + carry
            digit = s % 10
            carry = s // 10
            ans.append(str(digit))
            p1 -= 1
        while p2 >= 0:
            s = getInt(num2[p2]) + carry
            digit = s % 10
            carry = s // 10
            ans.append(str(digit))
            p2 -= 1
        if carry:
            ans.append(str(carry))
        return "".join(ans[::-1])
