import re
from bird_logic import bird_fly, bird_cry

def main():
    # user_input = "앵무새, 짹"
    user_input = input("새와 행동을 입력하시오. :")
    pattern = re.compile(r'[가-힣]+')              # 한글(가-힣)이 하나 이상 반복되는 문자열
    find_words = pattern.findall(user_input)      # findall() 함수를 사용하여 패턴과 일치하는 모든 문자열을 찾아 리스트로 반환

    if find_words[1] == "날기":
        bird_fly(find_words[0])
    elif find_words[1] == "짹":
        bird_cry(find_words[0])

if __name__ == "__main__":
    main()