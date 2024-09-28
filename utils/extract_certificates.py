import fitz  # PyMuPDF
import re
from pymongo import MongoClient

# MongoDB 연결 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['certificate_db']
collection = db['certificates']

def extract_certificate_info(pdf_path):
    """PDF에서 날짜와 수료증 이름을 추출하는 함수"""
    with fitz.open(pdf_path) as pdf_file:
        text = ""
        for page in pdf_file:
            text += page.get_text()

    # 날짜 추출 (예: YYYY-MM-DD 형식)
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    date_match = re.search(date_pattern, text)
    date = date_match.group() if date_match else "날짜 없음"

    # 수료증/자격증 이름 추출 (간단한 예: "수료증" 단어 포함)
    certificate_pattern = r"[\w\s]*(자격증|수료증)[\w\s]*"
    certificate_match = re.search(certificate_pattern, text)
    certificate_name = certificate_match.group() if certificate_match else "수료증/자격증 이름 없음"

    return {"date": date, "certificate_name": certificate_name}

def save_to_db(cert_info):
    """추출된 정보를 MongoDB에 저장"""
    collection.insert_one(cert_info)
    print("MongoDB에 저장 완료:", cert_info)

if __name__ == "__main__":
    # 예시 PDF 파일 경로
    pdf_path = "certificate_example.pdf"
    
    # PDF에서 정보 추출
    certificate_info = extract_certificate_info(pdf_path)
    
    # MongoDB에 저장
    save_to_db(certificate_info)
