def evaluate_operations(operations):
    x = 0
    for op in operations:
        if op == "X++" or op == "++X":
            x += 1
        else:
            x -= 1
    return x

n = int(input())
operations_list = [input() for _ in range(n)]
result = evaluate_operations(operations_list)
print(result)
