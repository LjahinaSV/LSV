from functools import reduce
print(
    reduce(
        lambda x, y: (x * y),
        map(
            lambda z: z ** 5,
            map(int, input().split())
        )
    )
)
