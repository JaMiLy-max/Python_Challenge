import pandas as pd
import random

cry_list = []

def bird_cry_list() -> list[dict]:
    ''' 
    새의 이름과 울음소리 정보를 받아옵니다.
    '''
    global cry_list
    if len(cry_list) > 0:
        return cry_list
    try:
        df_loaded = pd.read_csv('bird.csv', encoding='utf-8-sig')
        list_of_dicts = df_loaded.to_dict(orient='records')
        cry_list = list_of_dicts
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

    return cry_list

def bird_fly(bird_name):
    '''
    새를 날립니다.
    '''
    random_action = ["날고있습니다.", "자고있습니다", "날개가 부러졌습니다.", "날기싫어 뛰고있습니다."]
    random_weights = [0.7,0.1,0.1,0.1]  # 확률
    # random.choices() 함수를 사용하여 확률적으로 항목 선택
    if bird_name == "러버덕":
        action = "날지 않습니다."
    else:
        action = random.choices(random_action, weights=random_weights, k=1)[0]

    print(f'{bird_name}은(는) {action}')

def bird_cry(bird_name):
    bird_list = bird_cry_list()

    try:
        found_items = [tuple(item.values())[2:] for item in bird_list if item.get('새의 종류') == bird_name][0]
        print(f'{bird_name}가 "{random.choice(found_items)}" 울음소리를 냈습니다.')
    except IndexError or UnboundLocalError:
        print("새의 울음소리 정보를 찾을 수 없습니다.")

def bird_speed(bird_name, weight):
    bird_list = bird_cry_list()

    try:
        buff = 1
        found_items = [tuple(item.values())[1] for item in bird_list if item.get('새의 종류') == bird_name][0]
        
        if bird_name == "러버덕":
            print(f'{bird_name}는 속도가 0입니다. 달리지 못합니다.')
        else:
            if bird_name not in ("닭", "러버덕"):
                buff = 2
            
            print(f'{bird_name}는 "{found_items * weight * buff}" 의 속도로 달립니다.')
    except IndexError or UnboundLocalError:
        print("새의 속도 정보를 찾을 수 없습니다.")
    