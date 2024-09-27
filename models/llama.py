import requests
import json  # json 모듈 추가

def get_llama_model(prompt_text, temperature=0.9):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.1:8b",
        "prompt": prompt_text,
        "temperature": temperature
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, stream=True)  # 스트리밍 활성화

    full_response = ""
    for line in response.iter_lines():
        if line:
            # 각 라인의 JSON 데이터에서 텍스트 부분을 추출
            try:
                json_data = line.decode("utf-8")  # 문자열로 디코딩
                json_obj = json.loads(json_data)  # JSON 객체로 파싱 (requests.models.json 대신 json 모듈 사용)
                full_response += json_obj.get("response", "")  # "response" 필드 추가
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
    
    return full_response
