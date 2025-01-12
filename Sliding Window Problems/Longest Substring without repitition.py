def lengthOfLongestSubstring(s):
    seen={}
    left=0
    maxlength=0
    for right in range(len(s)):
        char=s[right]
        if(char not in seen):
            maxlength=max(maxlength,(right-left)+1)
        else:
            if(seen[char]<left):
               maxlength=max(maxlength,(right-left)+1) 
            else:
                left=seen[char]+1
        seen[char]=right
    
    return maxlength

print(lengthOfLongestSubstring("pwwkew"))