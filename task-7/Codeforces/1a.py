import math

def flagstones_needed(n, m, a):
    horizontal_flagstones = math.ceil(n / a)
    vertical_flagstones = math.ceil(m / a)

    total_flagstones = horizontal_flagstones * vertical_flagstones

    return total_flagstones

n,m,a= map(int,input().split())
print(flagstones_needed(n,m,a))