class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = False
        heavy = False
        dimensionLimit = 10**4
        volumeLimit = 10**9
        volume = length * width * height
        
        if any(x >= dimensionLimit for x in [length, width, height]) or volume >= volumeLimit:
            bulky = True
        
        if mass >= 100:
            heavy = True
        
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"