'''
크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061
'''

def solution(board, moves):
    answer = 0
    
    cnt = len(board)
    basket = []
    
    for move in moves:
        for depth in range(cnt):

            # 인형이 잡히는 경우
            if board[depth][move-1] != 0:
                # 바구니가 비어있을 때는 그냥 추가
                if len(basket) == 0:
                    basket.append(board[depth][move-1])
                    board[depth][move-1] = 0
                    print("move:",move, basket)
                    break
                # 바구니 안의 인형과 크레인이 잡은 인형이 같을 때
                if basket[len(basket)-1] == board[depth][move-1]:
                    board[depth][move-1] = 0
                    basket.pop()
                    answer += 2
                    print("move:",move, basket)

                    break
                # 다를 때
                else:
                    basket.append(board[depth][move-1])
                    board[depth][move-1] = 0
                    print("move:",move, basket)

                    break
                    
    return answer