from langchain.llms import OpenAI

def get_openai_model(temperature=0.9, model_name="gpt4o-mini"):
    # 모델 이름을 기본값으로 gpt4o-mini로 설정
    return OpenAI(temperature=temperature, model=model_name)
