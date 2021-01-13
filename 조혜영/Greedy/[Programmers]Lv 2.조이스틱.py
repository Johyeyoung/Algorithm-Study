def solution(name):
    answer = 0
    cnt_list = []
    # 조이스틱 위아래로 A에서 해당 문자까지 바꾸는 것만
    for x in name:
        cnt = min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)
        cnt_list.append(cnt)    
    answer += sum(cnt_list)
    print(answer)
    # 조이스틱 좌우 커서 이동하기
    idx = 0
    if 'A' in name:
        while True:
            leftstep, rightstep = 0, 0
            while True: # 왼쪽으로 A가 아닌 원소발견하게 step
                if cnt_list[idx - leftstep] != 0:
                    break
                else:
                    leftstep += 1

            while True: # 오른쪽으로 A가 아닌 원소발견하게 step
                if cnt_list[idx + rightstep] != 0:
                    break
                else:
                    rightstep += 1

            if leftstep < rightstep: #더 작은 보폭인쪽 선택
                idx -= leftstep
                answer += leftstep
            else:
                idx += rightstep
                answer += rightstep

            # A로 바꿔주는 코드 삽입하기
            cnt_list[idx] = 0

            if sum(cnt_list) == 0: #전체가 0되면 빠져나오기
                break
            
    else:
        answer += len(name) - 1    
    
    
    
    return answer
