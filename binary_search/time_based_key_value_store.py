from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.map = defaultdict(list) # 2 8 10^5 calls are made so this needs to run FAST
        
        # Knowing that they are strictly increasing makes me want to try and do binary search


    # all time stamps are strictly increasing
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        l = 0
        r = len(self.map[key])
    
        while l < r :
            m = l + (r - l) // 2
            if values[m][0] > timestamp :
                r = m
            else :
                l = m + 1

        return "" if r == 0 else values[l - 1][1]
         





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
