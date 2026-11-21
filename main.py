
from npu_sim.npu import mac, judge, measure_mac, EPSILON
from npu_sim.io_utils import read_mat, print_mat, load_json
from npu_sim.data_loader import normalize_label, get_size, normalize_filters

DATA = "data.json"


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

def mode2():
    print("#----------------------------------------")
    print("# [1] 필터 로드")
    print("#----------------------------------------")
    data = load_json(DATA)
    if data is None:
        print(f"{DATA}를 읽을 수 없어 프로그램을 종료합니다.")
        return 
    filters = normalize_filters(data)
    if filters is None:
        print("filters키를 찾을 수 없어 프로그램을 종료합니다.")
        return

    print("\n#----------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#----------------------------------------")
    
    t_cnt = len(data["patterns"].keys())   # test count
    p_cnt = 0   # pass count
    f_cnt = 0   # fail count
    case_dict = {}
    for key in data["patterns"].keys():
        pattern = data["patterns"][key]
        size = get_size(key)
        cross_filt = filters[size]["Cross"]
        x_filt = filters[size]["X"]
        cross_score = mac(pattern["input"], cross_filt)
        x_score = mac(pattern["input"], x_filt)
        result = judge(cross_score, x_score)   
        if result == "A": 
            result = "Cross"
        elif result == "B":
            result = "X"
        expected = normalize_label(pattern["expected"])
        if result == expected:
            Pass_Fail = "PASS"
            p_cnt += 1
        else:
            Pass_Fail = "FAIL"
            f_cnt += 1
            if result == "UNDECIDED":
                case_dict[key] = "동점(UNDECIDED)"
            else:
                case_dict[key] = "판정 불일치"

        print(f"\n--- {key} ---") 
        print(f"Cross 점수: {cross_score}")
        print(f"X 점수: {x_score}")
        print(f"판정: {result} | expected: {expected} | {Pass_Fail}")

    print("\n#----------------------------------------")
    print("# [3] 성능 분석 (평균/10회)")
    print("#----------------------------------------")
    sizes = sorted([3] + list(filters.keys()))
    print(f"{'크기':<8}{'평균 시간(ms)':>14}{'연산 횟수':>10}")
    print("-------------------------------------")
    for n in sizes:
        nxn = [[1.0 for _ in range(n)] for _ in range(n)]
        size = f"{n}x{n}"
        cal_vol = n*n
        _, avg_t = measure_mac(nxn,nxn)
        print(f"{size:<8}{avg_t:>14.4f}{cal_vol:>10}")

    print("\n#----------------------------------------")
    print("# [4] 결과 요약")
    print("#----------------------------------------")

    print(f"총 테스트: {t_cnt}개")
    print(f"통과: {p_cnt}개")
    print(f"실패: {f_cnt}개")
    print("실패 케이스:")
    for key, value in case_dict.items():
        print(f"  - {key}: {value}")
    
  
  


def main():
    mode = sel_mode()
    if mode == 1:
        mode1()
    elif mode == 2:
        mode2()


if __name__ == "__main__":
    main()

