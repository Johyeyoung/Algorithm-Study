def solution(s):
    max = 0
    for sub_len in range(1, len(s)+1): # 문자열의 길이
        # i는 sub string의 시작 인덱스
        for i in range(len(s) - sub_len + 1): # 조각의 개수만큼 ->이 방향으로 직진하면서 팰린드롬 여부 check
            if s[i:i+sub_len] == s[i:i+sub_len][::-1]: # 파이썬이라 한줄 가능 c++면 for문
                if max < sub_len:
                    max = sub_len
    return max



###################################DP 가능
# https://sewonkimm.github.io/algorithm/2019/09/19/longPal.html
