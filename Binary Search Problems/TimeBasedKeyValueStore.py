class TimeMap(object):
    def __init__(self):
        self.hashmap={}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if(self.hashmap.get(key) is None):
            self.hashmap[key]=[]
        self.hashmap[key].append([value,timestamp])
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        timeMap=self.hashmap.get(key)
        # print(timeMap)
        left=0
        right=(len(timeMap)-1)
        output=""
        while(left<=right):
            n=(left+right)//2
            # print(n)
            if(timeMap[n][1]==timestamp):
                return self.timeMap[n][0]
            elif(timestamp<timeMap[n][1]):
                right=n-1
            elif(timestamp>timeMap[n][1]):
                output=timeMap[n][0]
                    # print(output)
                left=n+1
            
        return output
            

                      
                 

obj = TimeMap()
obj.set("ctondw", "ztpearaw", 1)
obj.set("vrobykydll", "hwliiq", 2)
obj.set("gszaw", "ztpearaw", 3)
obj.set("ctondw", "gszaw", 4)
print(obj.hashmap)
print(obj.get("gszaw", 5))  # Expected output based on implementation
print(obj.get("ctondw", 6))  
print(obj.get("ctondw", 7))  
print(obj.get("gszaw", 8))  
print(obj.get("vrobykydll", 9))  
print(obj.get("ctondw", 10))  
obj.set("vrobykydll", "kcvcjzzwx", 11)
print(obj.get("vrobykydll", 12))  
print(obj.get("ctondw", 13))  
print(obj.get("vrobykydll", 14))  
obj.set("ztpearaw", "zondoubtib", 15)
obj.set("kcvcjzzwx", "hwliiq", 16)
obj.set("wtgbfvg", "vrobykydll", 17)
obj.set("hwliiq", "gzsiivks", 18)
print(obj.get("kcvcjzzwx", 19))  
print(obj.get("ztpearaw", 20))  
# print(obj.timeMap)

