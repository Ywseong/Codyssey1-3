def split(line, delim=" "): # delimiter를 기준으로 문자열을 나누어 리스트로 반환
    result = []
    src = ""
    for i in line:
        if i == delim:
            if src != "":
                result.append(src)
                src = ""
        else:
            src += i
    if src != "":
        result.append(src)
    return result