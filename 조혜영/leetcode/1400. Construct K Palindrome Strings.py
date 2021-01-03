class Solution(object):
    def canConstruct(self, s, k):
       
       # 문자의 개수보다 요구되는 k가 많으면 False
        if len(s) <k: return False
        
        # 항상 홀수개의 문자가 k에 영향을 줌 (짝수개는 그냥 상쇄)
        for i in set(s):
            if s.count(i)%2 != 0:
                k -= 1 # 홀수개의 문자가 요구된 k의 개수보다 많으면 조건을 만족하지 
            if k < 0:
                return False
        return True
