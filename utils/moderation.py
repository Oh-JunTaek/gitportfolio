import openai
from dotenv import load_dotenv
import os

# 환경 변수에서 API 키 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
