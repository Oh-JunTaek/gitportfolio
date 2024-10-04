from models.llama import get_llama_model

def display_keywords(keywords):
    """추출된 핵심 키워드를 사용자에게 표시"""
    print("\n추출된 키워드는 다음과 같습니다:")
    for keyword in keywords:
        print(f"- {keyword}")
    print("\n")

def get_user_input_for_keywords():
    """사용자로부터 자유 입력을 받아 키워드를 수정"""
    user_input = input("수정하거나 추가할 내용을 자유 형식으로 입력하세요 (ex: JAVA는 다루지 못하고 langchain 기술을 잘 다뤄.): ")
    return user_input

def refine_keywords(keywords, user_input):
    """사용자의 자유 입력을 기반으로 LLM을 사용해 키워드 재생성"""
    print("수정된 키워드를 분석하고 있습니다...")
    prompt = f"기존 키워드: {keywords}\n\n사용자의 입력: {user_input}\n\n이 정보를 바탕으로 새로운 핵심 키워드를 생성해 주세요."
    refined_keywords = get_llama_model(prompt)  # LLM 호출
    return refined_keywords.strip().split(",")

def get_user_confirmation(keywords):
    """사용자에게 키워드를 최종 확인받는 함수"""
    while True:
        display_keywords(keywords)
        modify = input("이 키워드 중 수정하거나 추가할 내용이 있습니까? (y/n): ")

        if modify.lower() == "y":
            user_input = get_user_input_for_keywords()
            keywords = refine_keywords(keywords, user_input)
        else:
            print("\n최종 키워드가 확인되었습니다.")
            return keywords