def isAnagram(s, t):
    count_s={}
    count_t={}
    for char in s:
        index=ord(char)
        if(index not in count_s):
            count_s[index]=index
        count_s[index]+=1
    for char in t:
        index=ord(char)
        if(index not in count_t):
            count_t[index]=index
        count_t[index]+=1
    if(count_s==count_t):
        return True
    return False

print(isAnagram("anagram","nagaram"))