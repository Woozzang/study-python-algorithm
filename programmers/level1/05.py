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