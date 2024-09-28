import fitz  # PyMuPDF for PDF handling
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# MongoDB 연결
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["resume"]  # 이력서 관련 DB
collection = db["certificates"]  # 자격증/수료증/공모전 내역 컬렉션

def save_document(type, name, date, organization):
    """
    자격증, 수료증, 공모전 내역을 MongoDB에 저장하는 함수
    """
    document = {
        "type": type,
        "name": name,
        "date": date,
        "organization": organization
    }
    collection.insert_one(document)
    print(f"{type} '{name}'가 MongoDB에 저장되었습니다.")

def extract_data_from_pdf(pdf_file):
    """
    PDF 파일에서 자격증/수료증 이름과 날짜를 추출하는 함수
    """
    try:
        with fitz.open(pdf_file) as pdf:
            text = ""
            for page_num in range(len(pdf)):
                page = pdf.load_page(page_num)
                text += page.get_text()

            # PDF 텍스트에서 이름과 날짜를 추출하는 로직
            name = extract_name_from_text(text)  # 이름 추출 (사용자 정의 함수 필요)
            date = extract_date_from_text(text)  # 날짜 추출 (사용자 정의 함수 필요)
            organization = "발급 기관 이름"  # 예시로 발급 기관을 지정

            return name, date, organization
    except Exception as e:
        print(f"PDF 파일을 처리하는 중 오류 발생: {str(e)}")
        return None, None, None

def extract_name_from_text(text):
    """
    PDF 텍스트에서 자격증/수료증 이름을 추출하는 예시 함수
    """
    return "추출된 자격증/수료증 이름"

def extract_date_from_text(text):
    """
    PDF 텍스트에서 발급 날짜를 추출하는 예시 함수
    """
    return "2024-01-01"  # 예시 날짜

def categorize_certificate(name, keywords):
    """
    자격증, 수료증, 대회를 분류하는 함수
    JSON에서 불러온 키워드를 기준으로 분류
    """
    certificate_keywords = keywords.get('certificates', [])
    award_keywords = keywords.get('awards', [])

    if any(keyword in name for keyword in certificate_keywords):
        return 'certificate'  # 자격증
    elif any(keyword in name for keyword in award_keywords):
        return 'award'  # 공모전 수상 내역
    else:
        return 'completion'  # 수료증

def load_keywords_from_json(file_path):
    """
    JSON 파일에서 자격증, 수료증, 공모전 키워드를 불러오는 함수
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"JSON 파일을 불러오는 중 오류 발생: {str(e)}")
        return None

if __name__ == "__main__":
    # JSON 파일 경로 지정
    json_file_path = "config/certificate_keywords.json"  # 적절한 경로로 설정

    # 자격증/수료증/공모전 키워드 로드
    keywords = load_keywords_from_json(json_file_path)

    # PDF 파일 경로 설정
    pdf_file = "sample_certificate.pdf"  # 자격증/수료증 PDF 파일 경로
    
    # PDF 파일에서 데이터 추출
    name, date, organization = extract_data_from_pdf(pdf_file)

    if name and date and keywords:
        # 이름을 기반으로 자격증/수료증/공모전으로 분류
        category = categorize_certificate(name, keywords)

        # MongoDB에 저장
        save_document(type=category, name=name, date=date, organization=organization)
    else:
        print("PDF에서 데이터를 추출할 수 없거나 키워드 로드에 실패했습니다.")
