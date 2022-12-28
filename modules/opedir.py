import os

def current_path():
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, '..'))
    print(base)
    print(name)

def get_current_path():
    base = os.path.dirname(os.path.abspath(__file__))
    return base

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
    current_path()
    print(get_current_path())
