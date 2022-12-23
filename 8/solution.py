# beats 85% runtime and 26% memory

class Solution:
    def myAtoi(self, s):
        neg=1
        c=""
        flag=0
        for i in s:
            if i==' ':
                if flag>0:
                    break
                continue
            elif i.isalpha():
                flag+=1
                break
            elif i=='+':
                flag+=1
                if flag>=2:
                    break
            elif i=='-':
                flag+=1
                if flag>=2:
                    break
                neg=-1
            else:
                flag+=1
                c+=i
        if c=="":
            return 0
        res=int(float(c))
        if -2147483648>res*neg:
            return -2147483648
        if 2147483647<res*neg:
            return 2147483647
        return res*neg