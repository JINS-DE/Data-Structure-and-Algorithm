import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
if k < 5:  # 필수 글자 5개를 배우지 못하면 0개 단어만 읽을 수 있음
    print(0)
    exit()

# 필수 글자
required = {'a', 'n', 't', 'i', 'c'}
li = []  # 읽을 수 있는 단어 집합 리스트
all_chars = set()  # 모든 단어에서 필수 글자를 제외한 문자들

for _ in range(n):
    inp = input().strip()
    tmp = set(inp[4:-4]) - required  # 단어에서 'anta'와 'tica'를 제거하고 필수 글자 제외
    li.append(tmp)
    all_chars.update(tmp)  # 전체 글자 집합 갱신

# 가능한 추가로 배울 수 있는 글자
extra_chars = list(all_chars)
if len(extra_chars) <= k - 5:  # 배울 수 있는 글자가 부족하면 모두 배우고 끝냄
    print(n)  # 모든 단어를 읽을 수 있음
    exit()

max_count = 0

# k-5개의 글자를 선택하는 모든 조합 탐색
for comb in combinations(extra_chars, k - 5):
    learned = set(comb)  # 현재 배운 글자
    count = 0

    # 각 단어가 읽을 수 있는지 확인
    for word in li:
        if word.issubset(learned):  # 단어의 모든 글자가 배운 글자에 포함되면 읽을 수 있음
            count += 1

    max_count = max(max_count, count)  # 최대 읽을 수 있는 단어 수 갱신

print(max_count)
