
size = ['3*3','4*4','5*5']
size_amp = [9,16,25]
mode_amp = [2,4]
score_h = []

#サイズ倍率、モード倍率、時間倍率から計算
def score(size_amp: int, mode_amp: int, time: int):
    total = 100
    total = total * size_amp * mode_amp
    score = total - time
    score_h.append(score)
    return score

#順位付け(降順で並び替え)
def juni(score):
    n = len(score)
    pivot = score[int(n / 2)]
 
    # i番目の値と基準値を比較して左l、右r、真ん中mに追加
    l = []
    r = []
    m = []
    for i in range(n):
        sample = score[i]
        if sample < pivot:
            l.append(sample)
        elif sample > pivot:
            r.append(sample)
        else:
            m.append(sample)
    # lとrの場合でそれぞれ再帰処理による分割を行う
    if l:
        l = juni(l)
    if r:
        r = juni(r)
    return l + m + r
    
    
if __name__ == '__main__':
    score(9,4,123)
    score(9,2,323)
    score(16,4,500)
    print(score_h)
    print(juni(score_h))
    

    
