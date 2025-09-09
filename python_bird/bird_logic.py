import pandas as pd
import random

def bird_cry_list() -> list[dict]:
    ''' 
    새의 이름과 울음소리 정보를 받아옵니다.
    '''
    df_loaded = pd.read_csv('bird.csv', encoding='utf-8-sig')
    list_of_dicts = df_loaded.to_dict(orient='records')

    return list_of_dicts

def bird_fly(bird_name):
    '''
    새를 날립니다.
    '''
    random_action = ["날고있습니다.", "자고있습니다", "날개가 부러졌습니다.", "날기싫어 뛰고있습니다."]
    random_weights = [0.7,0.1,0.1,0.1]  # 확률
    # random.choices() 함수를 사용하여 확률적으로 항목 선택
    action = random.choices(random_action, weights=random_weights, k=1)[0]

    print(f'{bird_name}은(는) {action}')

def bird_cry(bird_name):
    cry_list =  bird_cry_list()
    try:
        found_items = [tuple(item.values())[1:] for item in cry_list if item.get('새의 종류') == bird_name][0]
        print(f'{bird_name}가 "{random.choice(found_items)}" 울음소리를 냈습니다.')
    except IndexError or UnboundLocalError:
        print("새의 울음소리 정보를 찾을 수 없습니다.")
