

def tribonacci(self, n: int) -> int:
    mas = [0, 1, 1]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    for i in range(2, n):
        mas.append(mas[-1] + mas[-2] + mas[-3])
    return mas[-1]