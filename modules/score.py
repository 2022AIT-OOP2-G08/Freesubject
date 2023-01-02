import csv
score_h = []

def init():
    with open("././static/score.csv", "r", encoding="utf-8") as csv_file:
        #リスト形式
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        
        for row in f:
            score_h.append(row)

    return score_h



#サイズ倍率、モード倍率、時間倍率から計算
def score(size_amp: int, mode_amp: int, time: int):
    init()
    total = 100
    total = total * size_amp * mode_amp
    score = total - time
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
        if sample > pivot:
            l.append(sample)
        elif sample < pivot:
            r.append(sample)
        else:
            m.append(sample)
    # lとrの場合でそれぞれ再帰処理による分割を行う
    if l:
        l = juni(l)
    if r:
        r = juni(r)
    return l + m + r
    
def show():
    pass
    
if __name__ == '__main__':
    #print(init())
    score(9,4,123)
    score(9,2,323)
    score(16,4,500)
    
    

    
