class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []
        seen = set()
        last_occurance = {}
        for i in range(len(s)):
            last_occurance[ s[i] ] = i
        
        print(last_occurance)
        ## EXAMPLE : "cdadabcc"	##
		## STACK TRACE ##
        # {'c': 7, 'd': 3, 'a': 4, 'b': 5}
        # ['c']
        # ['c', 'd']
        # ['a']
        # ['a', 'd']
        # ['a', 'd', 'b']
        # ['a', 'd', 'b', 'c']
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            else:
                # 인덱스와 알파벳 모두 끝의 해당 원소보다 큰게 없어질 때까지 stack의 원소제거
                while( stack and stack[-1] > ch and last_occurance[stack[-1]] > i ):
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                # 해당 원소 추가
                seen.add(ch)
                stack.append(ch)
            print(stack)
        return ''.join(stack)
