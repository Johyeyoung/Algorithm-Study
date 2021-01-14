# 해당 문제 dp인데 dy배열에 저장하는 정보가 숫자가 아니라 list를 저장!
# 왜냐면 다음 bottom-up으로 다음 인덱스가 앞의 인덱스에 담긴 원소들을 이용하여 사칙연산하니까
# 사용하는 원소는 
def solution(N, number):
    # dy[idx] : idx개수의 N으로 만들수있는 모든 경우의 수 
    # base 조건 N==1의 경우 먼저 채우기: 인덱스 1부터하기위해 []-공백 채우기
    dy = [[],[N]]  # dy배열에 N을 idx개수로 표현할 수 있는 숫자들을 리스트를 담는다 
    if number == N: return 1 
    
    # 나머지 dy를 채우는데 문제 조건상 N의 사용횟수는 최대 8개!
    for i in range(2, 9):
        case_set = [int(str(N)*i)]
        # 랜선자르기 문제처럼 3 = (1,2), (2,1) 조각을 내서
        # N, 1개로 나올 수 있는 원소와 2개로 나올 수 있는 원소를 사칙연산
        for j in range(1, i):
            for k in dy[i-j]:
                for kk in dy[j]:
                    case_set.append(k * kk)
                    case_set.append(k + kk)
                    case_set.append(k - kk)
                    if kk != 0: case_set.append(k // kk)              
        # 탈출조건 = 총 i개의 원소로 구할 수 있는 경우를 다 case_set에 담은 뒤
        # 그중에 number가 있다면 더이상 그만 구해도 됨
        if number in case_set:
            return i
        dy.append(case_set) # dy배열에 list 정보를 저장 
    return -1


# top-down 보다 bottom-up이 어울리는 이유 N의 최소한의 개수로 나타내라니까 낮은 범위부터 채우게
