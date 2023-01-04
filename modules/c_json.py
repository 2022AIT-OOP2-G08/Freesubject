import json

def read_json():
    json_open = open('./static/setting.json', 'r')
    json_load = json.load(json_open)
    return json_load

def delete_json():
    jsonfile = read_json()
    jsonfile.clear()
    with open('./static/setting.json', 'w') as f:
        json.dump(jsonfile, f)
    

def update_json(dict: dict):
    jsonfile = read_json()
    jsonfile.update(dict)
    with open('./static/setting.json', 'w') as f:
        json.dump(jsonfile, f)
    

if __name__ == '__main__':
    update_json({'amp': 9})
    
    #delete_json()
    pass