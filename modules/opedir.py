import os

'''
実行場所の違いによるファイル操作のエラーを減らすために現在のディレクトリと親ディレクトリの絶対パスを取得する関数
'''

def show_cur_pare_path():
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, '..'))
    print(base)
    print(name)
#カレントディレクトリを取得
def get_current_path():
    base = os.path.dirname(os.path.abspath(__file__))
    return base
#親ディレクトリ(一つ上のディレクトリ)を取得
def get_parent_path():
    base = get_current_path()
    name = os.path.normpath(os.path.join(base, '..'))
    return name












#debug用コード
if __name__ == "__main__":
    images = 'sample.png'
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, '..'))
    print(base)
    print(name)
    print()
    show_cur_pare_path()
    print(get_current_path())
