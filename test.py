import math

def is_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def solve(n):
    nums = list(range(1, n + 1))
    permutation = []
    used = [False] * (n + 1)

    def backtrack():
        if len(permutation) == n:
            if is_square(permutation[0] + permutation[-1]):
                return True
            else:
                return False

        for i in range(1, n + 1):
            if not used[i]:
                if len(permutation) > 0:
                    if not is_square(permutation[-1] + i):
                        continue
                used[i] = True
                permutation.append(i)
                if backtrack():
                    return True
                permutation.pop()
                used[i] = False
        return False

    if backtrack():
        return permutation
    else:
        return -1

# Test cases
for n in range(1, 33):  # Test up to n=32, as the problem statement provides a solution for n=32
    result = solve(n)
    print(f"n = {n}: {result}")