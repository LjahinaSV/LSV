print(*
    map(
        lambda x, y: x ^ y,
        map(int, input().split()), map(int, input().split())

    )
)
# print(*map(lambda a, b: int(a != b), input().split(), input().split()))