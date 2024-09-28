import fitz  # PyMuPDF for PDF handling
from pymongo import MongoClient
from dotenv import load_dotenv
import os

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
            # 예시로, "자격증 이름", "발급일자"라는 패턴을 추출했다고 가정
            # 여기서는 간단한 텍스트 분석 로직을 추가할 수 있습니다.
            
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
    # 이 함수는 PDF 텍스트에서 적절한 이름을 추출하는 로직을 구현해야 합니다.
    # 간단한 예시로 특정 패턴이나 키워드로 이름을 추출할 수 있습니다.
    return "추출된 자격증/수료증 이름"

def extract_date_from_text(text):
    """
    PDF 텍스트에서 발급 날짜를 추출하는 예시 함수
    """
    # 이 함수는 PDF 텍스트에서 날짜를 추출하는 로직을 구현해야 합니다.
    return "2024-01-01"  # 예시 날짜

if __name__ == "__main__":
    # 자격증/수료증/공모전 정보를 PDF 파일로부터 추출하고 MongoDB에 저장하는 예시
    pdf_file = "sample_certificate.pdf"  # 자격증/수료증 PDF 파일 경로
    
    name, date, organization = extract_data_from_pdf(pdf_file)
    
    if name and date:
        # 자격증 데이터 저장
        save_document(type="certificate", name=name, date=date, organization=organization)
        
        # 수료증 데이터를 추가적으로 처리하고 싶다면 type을 "completion"으로 설정 가능
        # save_document(type="completion", name=name, date=date, organization=organization)

        # 공모전 수상 내역은 별도로 처리할 수 있습니다.
        # save_document(type="award", name="공모전 수상 내역", date="2024-01-15", organization="주최 기관")

    else:
        print("PDF에서 데이터를 추출할 수 없습니다.")
