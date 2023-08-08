def is_dangerous(positions):
    for i in range(len(positions)-6):
        if positions[i:i+7]=="0000000" or positions[i:i+7]=="1111111":
            return "YES"
    return "NO"

positions = input()
result = is_dangerous(positions)
print(result)
