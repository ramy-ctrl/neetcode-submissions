class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        flag = False
        while i>=0:
            if digits[i]<9:
                digits[i]+=1
                break
            else:
                digits[i]=0
                if i-1>=0:
                    i-=1
                else:
                    flag = True
        if flag == True:
            digits.append(0)
        return digits