def collatz_step(n):
    return n // 2 if n % 2 == 0 else n * 3 + 1


print(collatz_step(7))  # 22
