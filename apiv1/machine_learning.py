# ユーザーの最低音と最高音を取得する
import random

def main():
    lowest = random.randint(0, 8)
    highest = random.randint(lowest, 9)
    return lowest, highest

if __name__ == '__main__':
    main()