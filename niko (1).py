import math

# 1. Linear Search (Untuk data acak atau terurut)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. Binary Search Iteratif (Wajib data terurut)
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 3. Binary Search Rekursif (Wajib data terurut)
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)

# 4. Jump Search (Wajib data terurut)
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Mencari blok di mana target mungkin berada
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Melakukan Linear Search di dalam blok yang ditemukan
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# 5. Interpolation Search (Wajib terurut & terdistribusi seragam)
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Syarat tambahan: target harus berada di dalam rentang nilai array
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        # Rumus posisi interpolasi
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# --- AREA PENGUJIAN ---
if __name__ == "__main__":
    # Data harus terurut untuk Binary, Jump, dan Interpolation Search
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70

    print(f"Data: {data} | Target: {target}")
    print("-" * 40)
    print(f"Linear Search        : Index {linear_search(data, target)}")
    print(f"Binary (Iterative)   : Index {binary_search_iterative(data, target)}")
    print(f"Binary (Recursive)   : Index {binary_search_recursive(data, 0, len(data)-1, target)}")
    print(f"Jump Search          : Index {jump_search(data, target)}")
    print(f"Interpolation Search : Index {interpolation_search(data, target)}")