def max_apples(K, N, apple_sizes):
    apple_sizes.sort()  # Sort the apple sizes in ascending order
    max_apples_count = 0

    for i in range(N):
        for j in range(i, N):
            if apple_sizes[j] - apple_sizes[i] <= K:
                # If the difference between the largest and smallest apple is within the range K
                max_apples_count = max(max_apples_count, j - i + 1)

    return max_apples_count


# Example usage:
K = int(input().strip())
N = int(input().strip())
apple_sizes = [int(input().strip()) for _ in range(N)]

result = max_apples(K, N, apple_sizes)
print(result)
