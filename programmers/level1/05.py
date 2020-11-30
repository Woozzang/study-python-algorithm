def solution(answers):
    pat1 = [1,2,3,4,5]
    pat2 = [2,1,2,3,2,4,2,5]
    pat3 = [3,3,1,1,2,2,4,4,5,5]
    supo1 = 0
    supo2 = 0
    supo3 = 0

    for index, answer in enumerate(answers):
      if answer == pat1[index % 5]:
        supo1 += 1
      if answer == pat2[index % 8]:
        supo2 += 1
      if answer == pat3[index % 10]:
        supo3 += 1
    
    answer = []
    cnt = max(supo1, supo2, supo3)
    if(cnt == supo1):
      answer.append(1)
    if(cnt == supo2):
      answer.append(2)
    if(cnt == supo3):
      answer.append(3)

    return answer

# 개선 1

def solution_1(answers):
    pat1 = [1,2,3,4,5]
    pat2 = [2,1,2,3,2,4,2,5]
    pat3 = [3,3,1,1,2,2,4,4,5,5]
    # 3개의 관련된 변수를 하나의 list에 넣음
    score = [0, 0, 0]
    result = []

    for index, answer in enumerate(answers):
      if answer == pat1[index % 5]:
        score[0] += 1
      if answer == pat2[index % 8]:
        score[1] += 1
      if answer == pat3[index % 10]:
        score[2] += 1
    
    for index, s in enumerate(score):
        # 단, 평가식마다 max()를 호출하게 되어 score 길이에 따라 오버헤드가 될 수도 있음
        # max(score)은 고정된 값이므로 한번만 호출해서 변수에 저장해 놓는것이 나을 것이다.
        if s == max(score):
            result.append(index+1)

    return result