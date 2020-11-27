'''
완주하지 못한 선수
출처: https://programmers.co.kr/learn/courses/30/lessons/42576 
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1:
            return participant[i]
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]

# 개선 1
def solution(participant, completion):
    participant.sort()
    completion.sort()

    # line 11 에서 마지막 순회까지 돌경우 index error 나는 부분을 방지
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

# 개선 2
def solution(participant, completion):
    participant.sort()
    completion.sort()

    # zip () 의 이용
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    # participant[len(paticipant)-1] 보다 훨씬 간단한 코드
    return participant[-1]