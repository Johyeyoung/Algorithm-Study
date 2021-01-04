class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices % 2 != 0: 
            return []
        small = (4*cheeseSlices - tomatoSlices) // 2
        jumbo = cheeseSlices - small       
        return [jumbo, small] if jumbo>=0 and small>=0 else []
