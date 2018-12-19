#-*-coding:utf-8-*-
#!/usr/bin/python3

def hanoi(num_discs, start_peg, end_peg):
    other_peg = 6 - start_peg - end_peg
    if num_discs == 0:
        return
    else:
        hanoi(num_discs - 1, start_peg, other_peg)
        print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (num_discs, start_peg, end_peg))
        hanoi(num_discs - 1, other_peg, end_peg)

# 테스트 코드
hanoi(3, 1, 3)

# 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
# 가장 큰 원판을 start_peg에서 end_peg로 이동
# 나머지 원판들을 other_peg에서 end_peg로 이동
