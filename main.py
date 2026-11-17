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

    