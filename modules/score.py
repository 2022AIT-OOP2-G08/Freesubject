import csv

def read_csv():
    with open("././static/score.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            score_h = row
    return score_h

def write_csv(score_h):
    with open('././static/score.csv', 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(score_h)

#サイズ倍率、モード倍率、時間倍率から計算
def calc_score(size_amp: int, mode_amp: int, time: int):
    score_h = read_csv()
    total = 100
    total = total * size_amp * mode_amp
    score = total - time
    score_h.append(score)
    write_csv(score_h)#score.csvに上書き
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
    
    
if __name__ == '__main__':
    print(read_csv())
    #calc_score(9,4,123)
    #calc_score(9,2,323)
    #calc_score(16,4,500)
    
    
    