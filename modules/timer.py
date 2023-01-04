import time
start = 0
end = 0
def get_time():
    now_time = time.time
    return now_time 

def calc_time(start: float, end: float):
    time = abs(end - start)
    return time