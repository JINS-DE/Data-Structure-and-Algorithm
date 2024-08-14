def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # 왼쪽에서 오른쪽으로 이동하며 정렬
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1  # 끝이 정렬되었으므로 오른쪽 범위를 좁힘

        # 오른쪽에서 왼쪽으로 이동하며 정렬
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1  # 시작이 정렬되었으므로 왼쪽 범위를 좁힘

    return arr

# 예시
arr = [5, 1, 4, 2, 8, 0, 2]
sorted_arr = shaker_sort(arr)
print("정렬된 배열:", sorted_arr)