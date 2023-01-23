# Are you kidding me? It was that simple?
n, k, x = [int(x) for x in input().split()]
drops = []
min_drops = []
max_drops = []
for i in range(n):
    drops.append([int(x) for x in input().split()])
    min_drops.append(min(drops[i]))
    max_drops.append(max(drops[i]))

if sum(min_drops) >= x:
    print("ALWAYS")
elif sum(max_drops) < x:
    print("NEVER")
else:
    print("SOMETIMES")