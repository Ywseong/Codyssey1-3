import math

Filt_A = [[0,1,0],
          [1,1,1],
          [0,1,0]]
Filt_B = [[0,1,0],
          [1,1,1],
          [0,1,0]]
Filt_C = [[1,0,0],
          [1,0,1],
          [0,1,0]]
EPSILON = 1e-9

def mac(pattern, filt):
    add = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            mul = pattern[i][j]*filt[i][j]
            add += mul
    return add

def judge(filt_a, filt_b):
    if abs(filt_a-filt_b) < EPSILON:
        return "UNDECIDED"
    elif filt_a > filt_b:
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


    

print(read_mat(3))


    