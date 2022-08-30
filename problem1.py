from typing import List
A = 'hsyhag'
B = '2b12'
C = 'hsy2bhag1'


def isInterleave(A: str, B: str, C: str) -> bool:
    z=A+B
    if len(z)!=len(C):
      return False
    else:
        a=0
        b=0
        c=""
        for i in range (len(C)-1):
            if C[i]==A[a]:
                c=c+C[i]
                a=a+1
            elif C[i]==B[b]: 
                c=c+C[i]
                b=b+1 
            else :
                return False  
        if len(c)+1==len(C):
            return True     
          



print(isInterleave(A,B,C))      