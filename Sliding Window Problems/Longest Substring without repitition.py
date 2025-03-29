def lengthOfLongestSubstring(s):
    seen={None:None}
    left=0
    right=0
    length=0
    while(right<len(s)):
        while(s[right] in seen and left<right):
            del(seen[s[left]])
            left+=1
        
        seen[s[right]]=1
        length=max(length,right-left+1)
        right+=1
    return length

print(lengthOfLongestSubstring("pwwkew"))