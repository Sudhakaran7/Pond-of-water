class Solution(object):
    def canMeasureWater(self, x, y, z):
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)
        
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)
val=Solution()
a,b,water=map(int,input().split())
print(val.canMeasureWater(a,b,water))
