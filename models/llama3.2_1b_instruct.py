import torch
from transformers import LlamaForCausalLM, LlamaTokenizerFast

# 모델 및 토크나이저 경로 설정 (raw string 사용)
model_path = r"C:/Users/dev/.llama/checkpoints/Llama3.2-1B-Instruct/consolidated.00.pth"
tokenizer_path = r"C:\Users\dev\.llama\checkpoints\Llama3.2-1B-Instruct\tokenizer.model"

# 로컬 토크나이저 파일을 사용하여 토크나이저 로드
tokenizer = LlamaTokenizerFast(tokenizer_file=tokenizer_path)

# 모델 로드
model = torch.load(model_path, map_location=torch.device('cpu'))

# 입력 텍스트를 토큰화
input_text = "안녕하세요, 모델을 테스트합니다."
inputs = tokenizer(input_text, return_tensors="pt")

# 모델에 입력 전달하여 출력 생성
with torch.no_grad():
    outputs = model.generate(inputs["input_ids"], max_length=50)

# 출력된 토큰을 텍스트로 디코딩
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("모델 응답:", output_text)
