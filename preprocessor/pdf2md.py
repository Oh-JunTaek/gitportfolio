from pdfminer.high_level import extract_text

def convert_pdf_to_md(pdf_path):
    """PDF 파일을 MD 형식으로 변환하는 함수"""
    text = extract_text(pdf_path)
    md_content = "# PDF 내용\n\n" + text
    return md_content
