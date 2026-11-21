EPSILON = 1e-9

import time

def mac(pattern, filt):
    add = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            mul = pattern[i][j]*filt[i][j]
            add += mul
    return add

def judge(score_a, score_b):
    if abs(score_a-score_b) < EPSILON:
        return "UNDECIDED"
    elif score_a > score_b:
        return "A"
    else: 
        return "B"

def measure_mac(pattern, filt, repeat=10):
    result = mac(pattern, filt)
    whole_time = 0
    for _ in range(repeat):
        start = time.perf_counter()
        mac(pattern, filt)
        end = time.perf_counter()
        elapsed_time = end - start
        whole_time += elapsed_time
    return result, ((whole_time)/repeat*1000) # ms 단위로 변환