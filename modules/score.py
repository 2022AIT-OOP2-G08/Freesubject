#サイズ倍率、モード倍率、時間倍率から計算
def score(size_amp: int, mode_amp: int, time: int):
    total = 100
    total = total * size_amp * mode_amp
    score = total - time
    return score


size = ['3*3','4*4','5*5']
size_amp = [9,16,25]
mode_amp = [2,4]

if __name__ == '__main__':
    print(score(16,2,67))