from models.llama import get_llama_model
from utils.prompt import get_prompt_template
from utils.keywordprompt import get_star_keywords_prompt_template
from utils.github_api import get_repo_info
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# MongoDB 연결 설정
load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["resume"]  # DB 이름 설정
collection = db["resume_keywords"]  # 키워드 저장할 컬렉션 설정

def save_as_markdown(content, file_name="resume.md"):
    """답변을 .md 파일로 저장하는 함수"""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

def save_keywords_to_db(repo_name, keywords):
    """레포지토리 이름과 추출한 키워드를 MongoDB에 저장하는 함수"""
    document = {
        "repo_name": repo_name,
        "keywords": keywords
    }
    collection.insert_one(document)
    print(f"MongoDB에 {repo_name}의 키워드 저장 완료.")

if __name__ == "__main__":
    # GitHub 레포지토리 데이터를 처리하여 프롬프트에 넣을 데이터 생성
    repo_name = "Oh-JunTaek/MiniBaseball"  # 처리할 레포지토리
    repo = get_repo_info(repo_name)
    github_data = f"Repository Name: {repo.full_name}\nDescription: {repo.description}"

    # 1. 이력서 작성 프롬프트
    resume_prompt = get_prompt_template()
    resume_result = get_llama_model(resume_prompt.format(name="JunTaek Oh", github_data=github_data))

    # 2. STAR 키워드 추출 프롬프트
    keyword_prompt = get_star_keywords_prompt_template()
    keyword_result = get_llama_model(keyword_prompt.format(github_data=github_data))

    # 3. 결과를 .md 파일로 저장
    save_as_markdown(resume_result)
    print("이력서가 .md 파일로 저장되었습니다.")

    # 4. 키워드를 MongoDB에 저장
    save_keywords_to_db(repo_name, keyword_result)
    print("MongoDB에 키워드가 저장되었습니다.")
