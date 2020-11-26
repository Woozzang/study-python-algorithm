# N, M, K 를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번 째로 큰 수

print(first, second)

result = 0

while True:
  for i in range(k): # 가장 큰 수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩뺴기
  
  if m == 0: # m이 0이라면 반복분 탈출
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력

# O(km): k <= 10_000, m <= 10_000