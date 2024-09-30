from utils.confirm_keywords import get_user_confirmation
from utils.keywordprompt import get_star_keywords_prompt_template
from utils.prompt import get_prompt_template
from models.llama import get_llama_model
# from models.openAI import get_openai_model  # GPT4o-mini 모델 호출을 위한 import
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

def save_keywords_to_db(repo_names, all_keywords):
    """모든 레포지토리 이름과 통합된 키워드를 MongoDB에 저장하는 함수"""
    document = {
        "repo_names": repo_names,  # 모든 레포지토리 이름을 저장
        "keywords": all_keywords   # 통합된 모든 키워드를 저장
    }
    collection.insert_one(document)
    print("MongoDB에 모든 레포지토리의 키워드가 저장 완료되었습니다.")

if __name__ == "__main__":
    print("앱 실행 중...")

    # 사용자로부터 레포지토리 입력을 받음 (최대 4개)
    repos_input = input("분석할 GitHub 레포지토리들을 스페이스바로 구분하여 입력하세요 (최대 4개)[입력 예시 : Oh-JunTaek/MiniBaseball Oh-JunTaek/gitpotfolio]: ")

    # 스페이스바를 기준으로 레포지토리 이름을 나눔
    repo_names = repos_input.split(" ")

    # 최대 4개의 레포지만 처리하도록 제한
    if len(repo_names) > 4:
        print("최대 4개의 레포지토리만 분석할 수 있습니다.")
        repo_names = repo_names[:4]

    # 모든 레포지토리의 키워드를 저장할 리스트
    all_keywords = []

    # 각 레포지토리를 처리
    for repo_name in repo_names:
        print(f"토큰을 이용해 {repo_name} 정보를 불러오는 중입니다...")
        repo = get_repo_info(repo_name)
        github_data = f"Repository Name: {repo.full_name}\nDescription: {repo.description}"

        # STAR 키워드 추출 프롬프트 생성
        print(f"키워드 추출 중: {repo_name}")
        keyword_prompt = get_star_keywords_prompt_template()
        keyword_result = get_llama_model(keyword_prompt.format(github_data=github_data))
        keywords = keyword_result.strip().split(",")

        # 추출된 키워드를 통합 리스트에 추가
        all_keywords.extend(keywords)
        
        # GPT4o-mini 모델로 전환 시 주석 해제:
        # keyword_result = get_openai_model(model_name="gpt4o-mini").generate(keyword_prompt.format(github_data=github_data))

    print("모든 레포지토리에 대한 분석이 완료되었습니다.")

    # 2. 사용자와 키워드 수정 작업
    final_keywords = get_user_confirmation(all_keywords)

    # 3. 최종 키워드를 MongoDB에 저장
    save_keywords_to_db(repo_names, final_keywords)
    print("MongoDB에 키워드가 저장되었습니다.")

    # 4. 최종 이력서 작성
    print("이력서 작성 중입니다...")
    resume_prompt = get_prompt_template()

    # 최종 키워드를 이력서 생성에 반영
    resume_result = get_llama_model(resume_prompt.format(name="JunTaek Oh", github_data=f"레포지토리: {', '.join(repo_names)}\nKeywords: {', '.join(final_keywords)}"))
    
    # GPT4o-mini 모델로 전환 시 주석 해제:
    # resume_result = get_openai_model(model_name="gpt4o-mini").generate(resume_prompt.format(name="JunTaek Oh", github_data=f"레포지토리: {', '.join(repo_names)}\nKeywords: {', '.join(final_keywords)}"))

    save_as_markdown(resume_result)
    print("이력서가 .md 파일로 저장되었습니다.")
