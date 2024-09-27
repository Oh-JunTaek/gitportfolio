# gitportfolio
 
## 가상환경
1. 가상환경 생성
```
python -m venv gitpo
```
2.  For Mac 
```
source venv/bin/activate
```
3. For Windows
```
.\gitpo\Scripts\Activate
```

# GitPortfolio - GitHub 기반 이력서 생성기

이 프로젝트는 GitHub에서 사용자의 활동 데이터를 기반으로 이력서를 생성하는 도구입니다. FastAPI와 LangChain, 다양한 파일 형식(PDF, Markdown, DOCX, HWP)을 지원하며, STAR 기법을 사용하여 이력서를 작성합니다.

## 주요 기능

### 1. GitHub 데이터를 사용한 이력서 생성
GitHub API를 통해 사용자의 레포지토리 데이터를 수집하고, 이를 기반으로 STAR 기법으로 이력서를 생성합니다.

### 2. 다양한 파일 형식의 이력서 샘플 처리
이력서 샘플 파일이 PDF, Markdown(.md), DOCX, HWP 형식으로 제공될 수 있으며, 이를 처리하여 이력서 생성 시 참고합니다.

- **PDF**: PyMuPDF (`fitz`) 라이브러리를 사용하여 텍스트를 추출합니다.
- **Markdown**: 기본 `open` 함수로 파일을 읽어들입니다.
- **DOCX**: python-docx 라이브러리를 사용하여 DOCX 파일에서 텍스트를 추출합니다.
- **HWP**: `olefile`과 `pyhwp` 라이브러리를 사용해 HWP 파일을 처리하며, 두 가지 방법으로 실패율을 줄였습니다.

## 파일 처리 로직

## 사용방법
1. .env 파일에 GitHub API 토큰을 설정합니다.
```
GITHUB_TOKEN=your_github_token
```
2. 메인 스크립트를 실행하여 이력서를 생성하고 파일로 저장합니다.
```
python main.py
```
이 스크립트는 사용자의 GitHub 활동 데이터를 기반으로 이력서를 생성하며, 다양한 형식의 이력서 샘플을 참고하여 최적의 이력서를 만듭니다.

## 설치 및 의존성
필요한 패키지를 설치하려면 다음 명령어를 사용하세요
```
pip install -r requirements.txt
```

## 향후 계획 
1. 이력서 샘플 데이터를 RAG(검색 증강 생성) 기법으로 더 많은 샘플을 참고하여 이력서 품질을 향상시키는 기능 추가 예정.
2. GitHub 외부 데이터 소스와 연동하여 더 다양한 이력서 형식 지원.
3. 이력서 자동 번역 기능 추가 (다국어 지원).