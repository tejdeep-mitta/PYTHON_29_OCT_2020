def ispositive(n) -> bool:
    return n > 0


nums = [10, -10, 20, 50, -60]

for v in filter(ispositive, nums):
    print(v)
