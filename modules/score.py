import csv

def read_csv():#score_hをリスト型で返す
    score_h = []
    with open("./static/score.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        list = reader.__next__() #ヘッダーの読み込み
    for i in list:
        score_h.append(int(i))
    return score_h#list型

def write_csv(score):#リスト型のscore_hをcsvに書き込み
    score_h = juni(score)
    if len(score_h) > 5:#score_hが5より大きいとき残りを削除
        for num in range(len(score_h) - 5):
            score_h.pop(5)

    with open('./static/score.csv', 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(score_h)

#サイズ倍率、モード倍率、時間倍率から計算かつscore_hに追加かつcsvに書き込み
def calc_score(size_amp: int, mode_amp: int, time: int, score_h: list):
    total = 100
    total = total * size_amp * mode_amp
    score = total - time
    score_h.append(score)
    write_csv(score_h)
    return score


#順位付け(降順で並び替え)
def juni(score):
    score_h = sorted(score, reverse=True)
    return score_h
    
    
if __name__ == '__main__':
    print(read_csv())
    calc_score(25,10,1,read_csv())
    
    
    