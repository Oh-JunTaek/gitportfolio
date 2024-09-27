from github import Github
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# GITHUB_TOKEN 가져오기
github_token = os.getenv("GITHUB_TOKEN")

# GitHub 토큰으로 인증
g = Github(github_token)

def get_repo_info(repo_name):
    """레포지토리 이름을 받아 GitHub 레포지토리 정보를 반환"""
    repo = g.get_repo(repo_name)  # repo_name은 "Oh-JunTaek/MiniBaseball" 형태
    return repo