'''
두 개 뽑아서 더하기
출처: https://programmers.co.kr/learn/courses/30/lessons/68644
'''
def solution(numbers):
    answer = set()
    
    for index1 in range(len(numbers)):
        for index2 in range(len(numbers)):
            if index1 == index2:
                continue
            answer.add(numbers[index1] + numbers[index2])
            
    answer = list(answer)
    answer.sort()
    
    return answer
