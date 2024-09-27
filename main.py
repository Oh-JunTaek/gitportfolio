# from models.openai import get_openai_model
from models.llama import get_llama_model
from utils.prompt import get_prompt_template

# 프롬프트 설정
prompt = get_prompt_template()

# 모델 선택 (예: LLaMA 모델 사용)
result = get_llama_model(prompt.format(text="What is artificial intelligence?"))
print(result)
