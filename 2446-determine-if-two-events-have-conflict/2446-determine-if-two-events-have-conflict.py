class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def getMinutes(time: str) -> int:
            hours, minutes = time.split(":")
            
            return int(hours) * 60 + int(minutes)
        
        s1, e1 = getMinutes(event1[0]), getMinutes(event1[1])
        s2, e2 = getMinutes(event2[0]), getMinutes(event2[1])

        return (s2 <= s1 and s1 <= e2) or (s2 <= e1 and e1 <= e2) or (s1 <= s2 and s2 <= e1) or (s1 <= e2 and e2 <= e1)