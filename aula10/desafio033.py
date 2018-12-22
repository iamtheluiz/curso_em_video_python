# imports

print("""
|*****************|
|    Desafio33    |
|*****************|
""")
print("Qual é o maior?")

nums = []
while len(nums) < 3:
    count = len(nums)
    nums.append(float(input("Digite o {}º número: ".format(len(nums) + 1))))

nums.sort(reverse=True)

print()

print("Maior número: {}".format(nums[0]))
print("Menor número: {}".format(nums[2]))
print()
print("=====Rank=====")

i = 1
while len(nums) > 0:
    print("{}º = {}".format(i, nums[0]))
    nums.remove(nums[0])
    i += 1
