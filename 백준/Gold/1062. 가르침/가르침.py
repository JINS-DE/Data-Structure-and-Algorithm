import sys
from itertools import combinations

input = sys.stdin.readline
n, k = map(int, input().split())
word = {'a', 'n', 't', 'i', 'c'}  # 반드시 배워야 하는 글자
li = []  # 단어 목록
com = set()  # 조합에 사용할 글자 집합

# 입력 처리
for _ in range(n):
    input_word = input().strip()
    tmp = set(input_word[4:-4]) - word  # 단어에서 'antic'을 제외한 글자만 추출
    li.append(tmp)
    com.update(tmp)  # 전체 조합에 필요한 글자 추가

# k가 5보다 작으면 읽을 수 있는 단어 없음
if k < 5:
    print(0)
    sys.exit()

# 조합 가능한 글자의 개수는 k-5
max_count = 0
for comb in combinations(com, min(k - 5, len(com))):  # 최대 k-5개의 글자 조합 생성
    learn_set = word.union(comb)  # 'antic' + 현재 조합
    count = 0
    for word_set in li:
        if word_set <= learn_set:  # li 요소가 현재 부분집합에 속하는가?
            count += 1
    max_count = max(max_count, count)

print(max_count)
