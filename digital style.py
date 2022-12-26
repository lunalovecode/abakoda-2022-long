L, R = [int(x) for x in input().split()]
def calculate_digital_style(n):
    product = 1
    while n != 0:
        product *= n % 10
        n = n // 10
    return product

# Is it possible for the integer with the smallest "digital style" (the product of its digits) to be in between L and R?
# Let's say L is 2 and R is 1000.
# The minimum digital style is 1 because of 11.
# Well... shoot.

ans = 0
arr = []
for i in range(L, R + 1):
    if "0" in str(i):
        ans = 0
        break
    else:
        arr.append(calculate_digital_style(i))
        ans = min(arr)
print(ans)