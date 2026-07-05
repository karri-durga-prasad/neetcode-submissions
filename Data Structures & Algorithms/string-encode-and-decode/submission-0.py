class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            for j in i:
                s+=str(ord(j))
                s+=":"
            s+=","
        return s

    def decode(self, s: str) -> List[str]:
        l = s.split(",")
        t=[]
        for i in range(len(l)-1):
            m=''
            w=''
            for k in l[i]:
                if k!=":":
                    m+=k
                else:
                    w+=chr(int(m))
                    m=''
            t.append(w)
        return t
                
                
