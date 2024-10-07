import olefile
from docx import Document
import pdfplumber
import os

def convert_pdf_to_md(pdf_path, output_md_path):
    """PDF 파일을 Markdown으로 변환"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    print(f"페이지에서 텍스트를 추출할 수 없습니다: {page.page_number}")
    except Exception as e:
        print(f"PDF 변환 중 오류 발생: {e}")
        text = "PDF 변환 실패"

    # 텍스트를 .md 파일로 저장
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"PDF 변환 완료: {output_md_path}")

def convert_docx_to_md(docx_path, output_md_path):
    """DOCX 파일을 Markdown으로 변환"""
    try:
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"DOCX 변환 중 오류 발생: {e}")
        text = "DOCX 변환 실패"

    # 텍스트를 .md 파일로 저장
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"DOCX 변환 완료: {output_md_path}")

def convert_hwp_to_md(hwp_path, output_md_path):
    """HWP 파일을 Markdown으로 변환 (OLE 형식 사용)"""
    try:
        with olefile.OleFileIO(hwp_path) as ole:
            # HWP 파일의 OLE 스트림을 열어 텍스트 추출
            if ole.exists('BodyText/Section0'):
                text_stream = ole.openstream('BodyText/Section0')
                text = text_stream.read().decode('utf-16')  # 한글은 utf-16으로 인코딩됨
            else:
                text = "HWP 변환 실패: BodyText/Section0 존재하지 않음"
    except Exception as e:
        print(f"HWP 변환 중 오류 발생: {e}")
        text = "HWP 변환 실패"

    # 텍스트를 .md 파일로 저장
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"HWP 변환 완료: {output_md_path}")

def convert_to_md(file_path, output_dir):
    """파일 형식에 따라 적절한 변환 함수 호출"""
    if not os.path.exists(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return None

    file_ext = os.path.splitext(file_path)[1].lower()
    output_md_path = os.path.join(output_dir, os.path.basename(file_path).replace(file_ext, ".md"))

    try:
        if file_ext == ".pdf":
            convert_pdf_to_md(file_path, output_md_path)
        elif file_ext == ".docx":
            convert_docx_to_md(file_path, output_md_path)
        elif file_ext == ".hwp":
            convert_hwp_to_md(file_path, output_md_path)
        else:
            print(f"지원하지 않는 파일 형식입니다: {file_ext}")
            return None
    except Exception as e:
        print(f"파일 변환 중 오류 발생: {e}")
        return None

    return output_md_path

def convert_all_in_directory(input_dir, output_dir):
    """디렉토리 내의 모든 파일을 변환"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 출력 디렉토리가 없을 경우 생성

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):  # 파일인지 확인
            print(f"파일 변환 중: {filename}")
            convert_to_md(file_path, output_dir)

# 실행 예시
if __name__ == "__main__":
    input_directory = "data/raw"  # 원본 파일이 있는 디렉토리
    output_directory = "data/converted_md"  # 변환된 파일이 저장될 디렉토리

    convert_all_in_directory(input_directory, output_directory)
