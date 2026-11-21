
import math
from npu_sim.utils import split
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