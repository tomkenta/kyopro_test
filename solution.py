# -*- coding: utf-8 -*-

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
### 1000 = 1km
def solve():
    m = int(input())
    vv = 0
    if m < 100:
        vv = 0
    elif 100 <= m and m <= 5000:
        vv = m * 10
    elif 6000 <= m and m <= 30000:
        vv = m + 50000
    elif 35000 <= m and m <= 70000:
        vv = ((m - 30000) / 5) + 80000
    elif 70000 < m:
        vv = 89000

    output = int(vv / 1000)
    print("{0:02d}".format(output))


# solve()
##### ここまで
if __name__ == '__main__':
    solve()
