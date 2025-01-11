from collections import defaultdict
def groupAnagrams(strs):
    hashset=defaultdict(list)
    for string in strs:
        count=[0]*26
        for char in string:
            index=ord(char)-ord('a')
            count[index]+=1
        hashset[tuple(count)].append(string)
    
    return list(hashset.values())

strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))