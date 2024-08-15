import sys
n = int(input())
words = []
for _ in range(n):
    word = sys.stdin.readline()
    if word not in words:
        words.append(word)
arr = []
for i in range(len(words)):
    max_word = words[0]
    index = 0
    for j in range(1,len(words)-i):
        if (len(words[j]) == len(max_word) and words[j] > max_word) or len(words[j]) > len(max_word):
            max_word = words[j]
            index = j
    tmp = words[len(words)-i-1]
    words[len(words)-i-1] = words[index]
    words[index] = tmp
for word in words:
    sys.stdout.write(word)
