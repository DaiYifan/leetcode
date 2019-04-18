class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            t = -1
        else:
            t = 1
        y = abs(x)
        list = []
        z = 0
        while y!=0:
            list.append(y%10)
            y = int(y/10)
        l = len(list)
        for value in list:
            z = z + value*math.pow(10,l-1)
            l = l - 1
        if z > math.pow(-2,31) and z < (math.pow(2,31) - 1):
            return int(t*z)
        else:
            return 0
            
            # if y%10 != 0:
                # list.append(y%10)
            
                
            
        