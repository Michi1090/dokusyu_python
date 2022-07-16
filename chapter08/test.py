# 2
def get_square(base=1, height=1):
    return base * height

print(get_square())


# 3
def process_number(func, *nums):
    result = []
    for num in nums:
        result.append(func(num))

    return result

data = process_number(
    lambda num: num ** 2, 5, 3, 6
)

print(data)
