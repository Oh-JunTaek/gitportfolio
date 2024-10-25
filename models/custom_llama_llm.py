from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import requests
import json

class CustomLlamaLLM(LLM):
    model: str = "llama3.1:8b"
    url: str = "http://localhost:11434/api/generate"
    temperature: float = 0.9

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, json=payload, headers=headers, stream=True)

        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_data = line.decode("utf-8")
                    json_obj = json.loads(json_data)
                    full_response += json_obj.get("response", "")
                except ValueError as e:
                    print(f"Error decoding JSON: {e}")
        
        return full_response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {
            "model": self.model,
            "temperature": self.temperature
        }

    @property
    def _llm_type(self) -> str:
        # LLM 타입을 나타내는 문자열을 반환
        return "custom_llama_llm"

