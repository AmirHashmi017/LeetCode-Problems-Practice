def encode(strs):
    encoded=""
    for string in strs:
        encoded+=str(len(string))
        encoded+='#'
        encoded+=string
    return encoded
        
            
def decode(s):
    res = []
    i = 0
    while(i<len(s)):
        j=i
        while(s[j]!='#'):
            j+=1
        length=int(s[i:j])
        i=j+1
        j=i+length
        res.append(s[i:j])
        i=j
    return res

strs=["neet","code","love","you"]
encoded=encode(strs)
print(encoded)
print(decode(encoded))