import re, bird_logic as lg

def main():
    # user_input = "앵무새, 짹"
    user_input = input("새와 행동을 입력하시오. :")
    pattern = re.compile(r'[가-힣]+')              # 한글(가-힣)이 하나 이상 반복되는 문자열
    find_words = pattern.findall(user_input)      # findall() 함수를 사용하여 패턴과 일치하는 모든 문자열을 찾아 리스트로 반환

    # 입력값 유효성 검사
    if len(find_words) < 2:
        print("입력 형식이 올바르지 않습니다. '새이름, 행동' 형식으로 입력해주세요.")
        return

    bird_name, action = find_words[0], find_words[1]
    actions = {
        "날기": lg.bird_fly,
        "짹": lg.bird_cry,
        "달리기": lg.bird_speed,
    }

    if action in actions:
        if action == "달리기":
            try:
                weight = int(input(f"{bird_name}의 몸무게는 얼마입니까?(kg) :"))
                actions[action](bird_name, weight)
            except ValueError:
                print("몸무게는 숫자로 입력해야 합니다.")
        else:
            actions[action](bird_name)
    else:
        print(f"'{action}'은(는) 지원하지 않는 행동입니다.")
        
if __name__ == "__main__":
    main()