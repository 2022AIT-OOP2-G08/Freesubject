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
    #update_json({'amp': 9})
    #delete_json()
    pass