from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from models.custom_llama_llm import CustomLlamaLLM  # 사용자 정의 LLM 클래스 가져오기

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
        "repo_names": repo_names,
        "keywords": all_keywords
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

    # LangChain을 통한 Custom LLM 설정
    llm = CustomLlamaLLM()

    # 키워드 추출용 프롬프트 템플릿 설정
    keyword_template = """
    Given the GitHub repository information, extract key resume keywords:
    Repository Name: {repo_name}
    Description: {repo_description}
    """
    keyword_prompt = PromptTemplate(
        input_variables=["repo_name", "repo_description"],
        template=keyword_template,
    )
    keyword_chain = LLMChain(llm=llm, prompt=keyword_prompt)

    # 각 레포지토리를 처리
    for repo_name in repo_names:
        print(f"토큰을 이용해 {repo_name} 정보를 불러오는 중입니다...")
        repo = get_repo_info(repo_name)
        github_data = {
            "repo_name": repo.full_name,
            "repo_description": repo.description
        }

        # LangChain을 사용해 키워드 추출
        print(f"키워드 추출 중: {repo_name}")
        keyword_result = keyword_chain.run(**github_data)
        keywords = keyword_result.strip().split(",")
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

    # 사용자와 키워드 수정 작업
    final_keywords = get_user_confirmation(all_keywords)

    # 최종 키워드를 MongoDB에 저장
    save_keywords_to_db(repo_names, final_keywords)
    print("MongoDB에 키워드가 저장되었습니다.")

    # 이력서 샘플 프롬프트 템플릿 설정
    resume_template = """
    Generate a resume based on the extracted keywords and the following data:
    Name: {name}
    Experience Years: {experience_years}
    Project Name: {project_name}
    Description: {project_description}
    Technologies Used: {technologies_used}
    Achievements: {achievements}
    ...
    """
    resume_prompt = PromptTemplate(
        input_variables=[
            "name", "experience_years", "project_name", "project_description",
            "technologies_used", "achievements"
        ],
        template=resume_template,
    )
    resume_chain = LLMChain(llm=llm, prompt=resume_prompt)

    # 최종 이력서 작성
    print("이력서 작성 중입니다...")
    resume_result = resume_chain.run(**extracted_data)

    # 이력서를 .md 파일로 저장
    save_as_markdown(resume_result)
    print("이력서가 .md 파일로 저장되었습니다.")
