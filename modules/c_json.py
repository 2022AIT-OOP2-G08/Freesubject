import json

def read_json():#jsonファイルを読み込む
    json_open = open('./static/setting.json', 'r')
    json_load = json.load(json_open)
    return json_load

#画面1をロードしたときに行ってください
def init_json():#jsonファイルを初期化
    jsonfile = read_json()
    jsonfile.clear()
    with open('./static/setting.json', 'w') as f:
        json.dump(jsonfile, f)
    
#サイズ倍率、モード倍率、秒を保存するのに使ってください
def update_json(dict: dict):
    jsonfile = read_json()
    jsonfile.update(dict)
    with open('./static/setting.json', 'w') as f:
        json.dump(jsonfile, f)
    

if __name__ == '__main__':
    #main.py上での使用例
    #画面１
    #init_json():
    #画面4
    #update_json({"size_amp": n}) nは任意の倍率
    #update_json({"mode_amp": n}) nは任意の倍率
    #画面6
    #sec = int(timer.end - timer.start) ゲームにかかった秒数
    #update_json({'time': sec}) secは秒数
    #画面7
    #dict = read_json() このdictはそのあとにscore.pyにて使用

    pass