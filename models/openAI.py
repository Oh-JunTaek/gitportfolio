from langchain.llms import OpenAI
import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_model_and_check_moderation(prompt, temperature=0.9, model_name="gpt4o-mini"):
    """
    OpenAI 모델을 호출하고, 생성된 텍스트를 Moderation API로 검열하는 함수
    """
    # OpenAI 모델 설정 및 텍스트 생성
    llm = OpenAI(temperature=temperature, model=model_name)
    generated_text = llm(prompt)

    # 생성된 텍스트를 Moderation API로 검열
    flagged, categories = check_for_moderation(generated_text)
    
    if flagged:
        print(f"경고: 부적절한 콘텐츠 감지 - {categories}")
        return None  # 부적절한 경우 텍스트를 반환하지 않음
    else:
        return generated_text

def check_for_moderation(content):
    """
    OpenAI Moderation API를 통해 입력된 콘텐츠를 검열하는 함수
    """
    try:
        response = openai.Moderation.create(input=content)
        results = response["results"][0]
        # 'flagged'가 True이면 부적절한 콘텐츠가 포함된 것
        if results["flagged"]:
            return True, results["categories"]
        else:
            return False, None
    except Exception as e:
        print(f"Moderation API 호출 중 오류 발생: {str(e)}")
        return False, None

# 사용 예시
if __name__ == "__main__":
    prompt = "Create a friendly greeting message."
    response = get_openai_model_and_check_moderation(prompt)
    
    if response:
        print("모델 생성 결과:", response)
    else:
        print("부적절한 콘텐츠로 인해 결과가 반환되지 않았습니다.")
