from utils.confirm_keywords import get_user_confirmation
from utils.keywordprompt import get_resume_keywords_prompt_template  # 새로운 프롬프트로 변경
from prompt.resume_sample_prompt import get_resume_sample_prompt_template  # 이력서 샘플 프롬프트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from models.custom_llama_llm import CustomLlamaLLM 


from models.llama import get_llama_model
# from models.openAI import get_openai_model  # GPT4o-mini 모델 호출을 위한 import
from utils.github_api import get_repo_info
from utils.generate_resume import generate_resume
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
    extracted_data = {}
    
    llm = CustomLlamaLLM()

    # 각 레포지토리를 처리
    for repo_name in repo_names:
        print(f"토큰을 이용해 {repo_name} 정보를 불러오는 중입니다...")
        repo = get_repo_info(repo_name)
        github_data = f"Repository Name: {repo.full_name}\nDescription: {repo.description}"

        # 이력서 키워드 추출 프롬프트 생성
        print(f"키워드 추출 중: {repo_name}")
        keyword_prompt = get_resume_keywords_prompt_template()  # 프롬프트 생성
        keyword_result = get_llama_model(keyword_prompt.format(github_data=github_data))
        keywords = keyword_result.strip().split(",")


        # 추출된 키워드를 통합 리스트에 추가
        all_keywords.extend(keywords)

        # extracted_data에 레포지토리 관련 데이터를 추가
        extracted_data = {
            "name": "JunTaek Oh",  # 실제 추출한 데이터로 대체 가능
            "experience_years": "2020",
            "experience_years_end": "2024",
            "project_name": repo.full_name,
            "project_description": repo.description,
            "technologies_used": "Android, Java",  # 필요한 경우 업데이트
            "education_start": "2020",
            "education_end": "2024",
            "degree_name": "Bachelor of Science in Computer Science",
            "award_date": "2023",
            "award_name": "AI Hackathon Winner",
            "project_name_award": repo.full_name,
            "achievements": "Developed an Android game",  # 레포지토리별로 수정 가능
            "project_start": "2023",
            "project_end": "2024",
            "project_title": "AI-Powered Game Development",
            "project_technologies": "LangChain, GPT-3, Python",
            "project_achievements": "Created an AI-powered game development workflow"
        }

    print("모든 레포지토리에 대한 분석이 완료되었습니다.")

    # 2. 사용자와 키워드 수정 작업
    final_keywords = get_user_confirmation(all_keywords)

    # 3. 최종 키워드를 MongoDB에 저장
    save_keywords_to_db(repo_names, final_keywords)
    print("MongoDB에 키워드가 저장되었습니다.")

    # 4. 최종 이력서 작성
    print("이력서 작성 중입니다...")
    
    # 이력서 샘플 프롬프트를 사용하여 이력서 생성
    resume_prompt = get_resume_sample_prompt_template()

    # 별도로 만든 이력서 생성 함수를 호출
    resume_result = generate_resume(resume_prompt, extracted_data, final_keywords, repo_names)
    
    # 이력서를 .md 파일로 저장
    save_as_markdown(resume_result)
    print("이력서가 .md 파일로 저장되었습니다.")

