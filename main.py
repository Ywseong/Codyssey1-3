import math
import time
EPSILON = 1e-9

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
def split(line):
    result = []
    src = ""
    for i in line:
        if i == " ":
            if src != "":
                result.append(src)
                src = ""
        else:
            src += i
    if src != "":
        result.append(src)
    return result

def read_mat(n): ###########################
    mat = []
    re = " "

    while len(mat) < n:
        try:
            mat = []
            
            print(f"{n} x {n} 행렬을{re}입력하시오") 
            for _ in range(n):
                line = input()
                entry = split(line)
                if len(entry) != n:
                    print(f"\n{n}개의 요소를 입력하세요")
                    re = " 다시 "
                    break
         
                row = list(map(float,entry)) # value 에러 발생 가능
                ok = True
                for num  in row:    
                    if not math.isfinite(num):
                        print("\nnan과 inf는 허용되지 않습니다.")
                        re = " 다시 "
                        ok = False
                        break
                if ok:
                    mat.append(row)
                    
                else:
                    break
        except ValueError:
            print("\n실수를 입력하시오")
            re = " 다시 "
    return mat

def print_mat(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

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

def sel_mode():
    print("=== Mini NPU Simulator ===\n")
    print("[모드 선택]")
    print("1. 사용자 입력(3x3)")
    print("2. data.json 분석")
    while True:
        try:
            mode = int(input("선택: "))
            if mode in [1, 2]:
                break
            print("1 또는 2를 입력하세요.")
        except ValueError:
            print("정수를 입력하세요.")
    print()
    return mode

def mode1():
    print("#----------------------------------------")
    print("# [1] 필터 입력")
    print("#----------------------------------------")


    print("필터 A (3줄 입력, 공백 구분)")
    filt_a = read_mat(3)
    print("\n입력된 필터 A:")
    print_mat(filt_a)

    print("\n필터 B (3줄 입력, 공백 구분)")
    filt_b = read_mat(3)
    print("\n입력된 필터 B:")
    print_mat(filt_b)

    print("\n#----------------------------------------")
    print("# [2] 패턴 입력")
    print("#----------------------------------------")

    print("패턴 (3줄 입력, 공백 구분)")
    pattern = read_mat(3)
    print("\n입력된 패턴:")
    print_mat(pattern)

    print("\n#----------------------------------------")
    print("# [3] MAC 결과")
    print("#----------------------------------------")

    mac_a, time_a = measure_mac(pattern, filt_a)
    mac_b, time_b = measure_mac(pattern, filt_b)
    time_avg = (time_a + time_b) / 2

    print(f"A 점수: {mac_a}")
    print(f"B 점수: {mac_b}")
    print(f"연산 시간(평균/10회): {time_avg:.4f} ms")

    result = judge(mac_a, mac_b)

    if result == "UNDECIDED":
        print(f"판정: 판정 불가 (|A-B| < {EPSILON})")
    else:
        print(f"판정: {result}")

def main():
    mode = sel_mode()
    if mode == 1:
        mode1()
    elif mode == 2:
        print("data.json 분석 모드는 아직 구현되지 않았습니다.")
if __name__ == "__main__":
    main()

