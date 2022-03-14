class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.diffWaysToComputeHelper({}, expression)

    def diffWaysToComputeHelper(self, hashmap: Dict, expression: str) -> List[str]:
        if expression in hashmap:
            return hashmap[expression]
        res = []
        # if input is a number, parse it and add to output
        if expression.isnumeric():
            res.append(int(expression))
        else:
            for i in range(len(expression)):
                # if one of "+", "-", or "*"
                char = expression[i]
                if not char.isdigit():
                    # break eqn into 2 parts and make recursive calls
                    left = self.diffWaysToCompute(expression[0:i])
                    right = self.diffWaysToCompute(expression[i + 1 :])
                    for p1 in left:
                        for p2 in right:
                            if char == "+":
                                res.append(p1 + p2)
                            elif char == "-":
                                res.append(p1 - p2)
                            elif char == "*":
                                res.append(p1 * p2)
        hashmap[expression] = res
        return res
