def next_round(n, k, scores):
    advanced_count = 0
    for score in scores:
        if score >= scores[k-1] and score > 0:
            advanced_count += 1
    return advanced_count

n, k = map(int, input().split())
scores = list(map(int, input().split()))

result = next_round(n, k, scores)

print(result)
