def solution(user_id, banned_id):
    answer_set = set()
    user_size = len(user_id)
    ban_size = len(banned_id)
    
    def check(a, b):
        # 문자열 a가 b 패턴에 맞는지 확인
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if b[i] != '*' and a[i] != b[i]:
                return False
        return True

    def dfs(depth, path, used):
        if depth == ban_size:
            # frozenset을 써서 순서 상관없는 조합으로 중복 제거
            answer_set.add(frozenset(path))
            return
        for i in range(user_size):
            if not used[i] and check(user_id[i], banned_id[depth]):
                used[i] = True
                dfs(depth + 1, path + [user_id[i]], used)
                used[i] = False

    used = [False] * user_size
    dfs(0, [], used)
    return len(answer_set)
