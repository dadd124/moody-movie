import os
from openai import OpenAI
import re
import openai


# OpenAI API 클라이언트 초기화
# YOUR_API_KEY 대신 실제 API 키를 입력하거나 환경 변수로 설정해야 합니다.
# 예: os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key="OPENAI_API_KEY")

# 테스트용입니다
# GPT에게 요청을 보내고 응답을 받는 함수
def get_gpt_response(situation_description, user_input_text="",
                      persona_description="너는 영화를 추천해주는 챗봇이야. 기본적으로는 감정을 기반으로 추천해주지만,"
                      "사용자가 원한다면 장르와 배우, 년도를 기반으로 영화를 추천해줄 수 있어. 기본적으로 한두 개의 영화를 추천해주며, 뒤에 그 이유를 붙여줘.",
                        model_name="gpt-4o-mini"):
    """
    GPT에게 상황 설명을 전달하고 자연스러운 응답을 받아옵니다.

    Args:
        situation_description (str): GPT가 이해해야 할 현재 상황이나 의도.
        user_input_text (str, optional): 사용자의 입력이 답변 생성에 필요한 경우 추가.
        persona_description (str, optional): GPT의 페르소나 설정. 기본값은 "길잡이".
        model_name (str, optional): 사용할 GPT 모델 이름. 기본값은 gpt-4o-mini.

    Returns:
        str: GPT가 생성한 답변.
    """
    try:
        messages = [
            {"role": "system", "content": persona_description},
            {"role": "user", "content": f"상황: {situation_description}"}
        ]
        
        # 만약 사용자의 입력이 답변 생성에 중요하다면 user_input_text를 프롬프트에 포함합니다.
        if user_input_text:
             messages[1]["content"] += f"\n사용자 입력: {user_input_text}"

        chat_completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.8,  # 창의성 조절 (0.0은 보수적, 1.0은 매우 창의적)
            max_tokens=300,    # 응답의 최대 길이 조절
        )

        return chat_completion.choices[0].message.content.strip()
    except openai.error.AuthenticationError:
        print(f"API 인증 오류 발생. 키를 확인해주세요.")
        return "API 인증 오류가 발생했어요. 키를 확인해주세요."
    
    except openai.error.RateLimitError:
        print(f"서버 요청이 많아요. 잠시 후 다시 시도해주세요.")
        return "서버 요청이 많아요. 잠시 후 다시 시도해주세요."

    except Exception as e:
        print(f"GPT 응답을 가져오는 중 오류 발생: {e}")
        return "GPT가 잠시 생각에 잠겼나 봐. 다시 시도해줄래?"

end_keywords = ["끝내","끝낼","여기까지" ]
genre_keywords = ["장르", "액션", "로맨스", "코미디", "스릴러", "공포", "SF"]
genre_vowel = ["액션", "코미디", "드라마", "로맨스", "스릴러", "공포", "범죄", "SF", "공상과학", "사이버펑크", "스팀펑크", "판타지", "다큐멘터리"]
actor_keywords = ["배우", "출연", "주연", "출연진", "배우로", "연기한"]
emotion_keywords = ["감정", "감성", "기분"]
reset_keywords = ["처음", "맨앞", "리셋", "맨 앞"]
director_keywords = ["감독", "연출가", "연출", "메가폰", "감독님", "감독이"]
want_keywords = ["원하는 것", "원하는", "원해", "원합니다", "원해요", "바래", "바람", "바랍니다", "바래요"]
year_keywords = ["년도", "옛날", "최신", "년"]
satisfaction_keywords = ["만족", "좋았", "좋았다", "좋아요", "끝내", "짱", "최고"]
dissatisfaction_keywords = ["불", "아니", "불만족", "불만", "최악", "별로", "내키지", "아쉬", "아쉽", "실망"]
info_keywords = ["정보", "영화 정보", "있어", "?"]
actor_names = [
    "송강호", "마동석", "전도연", "이병헌", "공유", "조진웅",
    "톰 크루즈", "레오나르도 디카프리오", "스칼렛 요한슨",
    "브래드 피트", "로버트 다우니 주니어"
]
director_names = [
    "봉준호", "박찬욱", "이창동", "나홍진", "임권택",
    "최동훈", "류승완", "김한민", "김용화", "정병길",
    "크리스토퍼 놀란", "스티븐 스필버그", "타란티노", "제임스 카메론"
]

result = ''

def main_menu():
    
    global result
    while True:
        if result == "exit":
            break

        print("\n감정 측정 중 예외.")

        situation = "감정을 통한 영화 추천이 아니라 다른 방식을 원하는 것 같아. 잠시 추천을 멈추고 장르나 배우, 감독, 또는 영화 정보 중에서 필요한 정보를 고르게 해보자."
        response = get_gpt_response(situation)
        user_input = input(response)

        if any(k in user_input for k in genre_keywords):
            situation = "사용자가 감정이 아닌 장르를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자가 감정이 아닌 영화에 출연하는 배우를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        elif any(k in user_input for k in year_keywords):
            situation = "사용자는 감정이 아닌 년도를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            year()

        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()
        
        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()


def genre(): # 장르
    while True:
        user_input = input(": ")

        if any(k in user_input for k in year_keywords):
            situation = "사용자가 장르가 아닌 년도를 기준으로 영화를 고르고 싶어하는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            year()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자는 배우를 기준으로 영화를 보고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        elif any(k in user_input for k in emotion_keywords):
            situation = "다시 감정을 기준으로 영화를 고르려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            emotion()

        elif any(k in user_input for k in reset_keywords):
            situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return

        elif any(k in user_input for k in want_keywords) or any(k in user_input for k in genre_vowel):
            situation = "사용자가 지시한 사항에 맞춰 영화를 추천해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            survey()

        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()

        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()

def actor_list(text):
    if any(name in text for name in actor_names):
        return True
    
    name_pattern = re.compile(r'^[가-힣]{2,}(?:\s[가-힣]{2,})?$')
    if name_pattern.match(text.strip()):
        return True
    
    return False

def actor(): # 배우
    while True:
        user_input = input(": ")

        if actor_list(user_input):
            situation = f"사용자가 '{user_input}' 배우의 영화를 추천해달라고 하는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            survey()

        elif any(k in user_input for k in actor_keywords):
            situation = "배우가 아닌 장르를 기준으로 영화를 택하려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in emotion_keywords):
            situation = "다시 감정을 기준으로 영화를 고르려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            emotion()

        elif any(k in user_input for k in reset_keywords):
            situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return
        
        elif any(k in user_input for k in want_keywords):
            situation = "사용자가 지시한 사항에 맞춰 영화를 추천해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            survey()

        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()

def wrong_answer(): # 예상 밖의 답변
    while True:
        user_input = input(": ")

        if any(k in user_input for k in genre_keywords):
            situation = "사용자가 장르를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자가 배우를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        elif any(k in user_input for k in reset_keywords):
            situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return
        
        elif any(k in user_input for k in year_keywords):
            situation = "사용자가 다시 년도를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            year()

        elif any(k in user_input for k in emotion_keywords):
            situation = "다시 감정을 기준으로 영화를 고르려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            emotion()


        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()

        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            continue

def emotion(): # 감정 롤백
    while True:
        user_input = input(": ")

        if any(k in user_input for k in genre_keywords):
            situation = "사용자가 다시 장르를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자가 다시 배우를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        elif any(k in user_input for k in reset_keywords):
            situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return
        
        elif any(k in user_input for k in want_keywords):
            situation = "사용자가 지시한 사항에 맞춰 영화를 추천해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            survey()

        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()
            
        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()

def survey(): # 만족, 불만족 물어보기
    situation = "사용자에게 영화 추천은 만족했는지 물어봐봐. 되도록 만족, 불만족 쪽으로 답변을 해줬으면 좋겠다는 말도 친절하게 덧붙여줘."
    response = get_gpt_response(situation)
    print(response)
    user_input = input("")

    if any(k in user_input for k in satisfaction_keywords):
        situation = "사용자가 말한 만족도에 맞춰 반응해줘. 바로 영화를 추천하지 말고 추가적인 영화 추천이 필요한지 물어봐 줘."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        push()

    elif any(k in user_input for k in dissatisfaction_keywords):
        situation = "사용자가 만족도가 아쉽다고 전하고 있어. 영화를 추천하지 말고 공감과 위로의 멘트를 전해줘."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        end()

    else:
        situation = "만족도를 말하지는 아쉽다고 말하고 추가적인 영화 추천이 필요한지 물어봐 줘."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        push()

def suggestion(user_input):
    positive_keywords = ["추가", "더", "또", "필요", "해줘", "좋아", "응", "그래", "그럴래"]
    negative_keywords = ["괜찮", "필요없", "싫", "그만", "됐어", "아니", "별로", "없어"]

    if any(k in user_input for k in positive_keywords):
        return "yes"
    elif any(k in user_input for k in negative_keywords):
        return "no"
    else:
        return "unclear"

def push(): # 추가적인 추천
        situation = "사용자에게 추가적인 추천이 필요한지 물어봐줘."
        response = get_gpt_response(situation)
        print(response)
        user_input = input(": ")
        sug = suggestion(user_input)

        if sug == "yes":
            situation = "사용자가 추가적인 영화 추천을 원하고 있어. 바로 추천하지는 말고 원하는 구체적인 방향성을 물어봐줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            addition()

        elif sug == "no":
            situation = "사용자가 더 이상 추천을 원하지 않아. 너는 긍정을 하고 마무리 인사를 준비해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            end()

        else:
            situation = "사용자의 의도가 애매해. 따라서 자연스럽게 대화를 마무리하는 방향으로 잡아줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            end()

def year(): # 년도

    user_input = input(": ")

    has_year_number = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', user_input)

    if any(k in user_input for k in year_keywords) or has_year_number:
        situation = "사용자가 입력한 년도에서 영화를 추천해줘."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        survey()

    elif any(k in user_input for k in genre_keywords):
        situation = "사용자가 다시 장르를 기반으로 영화를 추천 받고 싶나 봐."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        genre()

    elif any(k in user_input for k in actor_keywords):
        situation = "사용자가 다시 배우를 기반으로 영화를 추천 받고 싶나 봐."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        actor()

    elif any(k in user_input for k in reset_keywords):
        situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        return
    
    elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()
    
    elif any(k in user_input for k in emotion_keywords):
            situation = "다시 감정을 기준으로 영화를 고르려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            emotion()
    else:
        situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        wrong_answer()

def end(): # 종료
        global result
        user_input = input(": ")
        situation = "적절한 마무리 인사로 대응해줘. 이제 영화 추천은 그만하고, 작별 인사만 해줘."
        response = get_gpt_response(situation, user_input_text=user_input)
        print(response)
        result = "exit"

def addition(): # 추가 추천
        user_input = input(": ")

        if any(k in user_input for k in reset_keywords):
            situation = "사용자가 처음부터 다시 천천히 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return
        
        else:
            situation = "사용자가 요청한 요구에 맞춰서 영화를 추천해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            survey()

def directors_names(text):
    return any(name in text for name in director_names)

def director(): # 감독
        user_input = input(": ")

        if any(k in user_input for k in want_keywords) or directors_names(user_input):
            situation = "사용자의 지시에 맞춰 영화를 추천해줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            push()

        elif any(k in user_input for k in reset_keywords):
            situation = "다시 처음으로 돌아가서 영화를 고르고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            return
        
        elif any(k in user_input for k in genre_keywords):
            situation = "사용자가 다시 장르를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in emotion_keywords):
            situation = "다시 감정을 기준으로 영화를 고르려고 하나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            emotion()
        
        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자가 다시 배우를 기반으로 영화를 추천 받고 싶나 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()
    
def information(): # 영화 정보 요청 시
        user_input = input(": ")

        if user_input:
            situation = "사용자가 요청한 정보를 가져와서 이야기해줘. 추가로 궁금한 점이 있는지 물어봐줘."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)            
            information_since()

def information_since(): # 영화 정보 전달 이후 선택지
        situation = "사용자가 원하는 정보를 얻었어. 그러니 잠시 추천을 멈추고 다음에 할 선택을 물어봐 줘."
        response = get_gpt_response(situation)
        user_input = input(f"{response}\n: ")

        if any(k in user_input for k in genre_keywords):
            situation = "사용자가 감정이 아닌 장르를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            genre()

        elif any(k in user_input for k in actor_keywords):
            situation = "사용자가 감정이 아닌 영화에 출연하는 배우를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            actor()

        elif any(k in user_input for k in year_keywords):
            situation = "사용자는 감정이 아닌 년도를 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            year()

        elif any(k in user_input for k in director_keywords):
            situation = "사용자가 감정이 아닌 감독을 기반으로 영화를 추천 받고 싶은 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            director()
        
        elif any(k in user_input for k in info_keywords):
            situation = "사용자가 추가적인 영화 정보가 있는지 물어보고 있는 것 같아."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)   
            information()

        else:
            situation = "사용자가 기획과 다르게 엉뚱한 요구를 했나 봐. 최대한 다시 영화 추천 하는 쪽으로 대화를 유도해 봐."
            response = get_gpt_response(situation, user_input_text=user_input)
            print(response)
            wrong_answer()


if __name__ == "__main__":
    main_menu()

