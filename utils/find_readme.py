import requests
from github import Github  # GitHub API를 사용하기 위한 모듈
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# GitHub 토큰 가져오기
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# GitHub API 인증
g = Github(GITHUB_TOKEN)

def get_github_profile_readme(username):
    """
    GitHub 사용자의 프로필 README 파일의 내용을 가져옵니다.
    
    :param username: GitHub 사용자 이름
    :return: README 파일의 내용
    """
    # GitHub API URL 설정
    url = f"https://api.github.com/repos/{username}/{username}/readme"
    
    # 요청 헤더에 토큰을 포함시켜 인증 정보 제공
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.raw"  # Raw 컨텐츠 형식으로 데이터 요청
    }
    
    # GitHub API에 요청
    response = requests.get(url, headers=headers)
    
    # 요청이 성공적인지 확인
    if response.status_code == 200:
        return response.text  # README 파일의 내용을 텍스트로 반환
    else:
        return f"README 파일을 가져오는 데 실패했습니다. 에러 코드: {response.status_code}"

def get_user_repos(username):
    """특정 사용자의 모든 레포지토리 목록을 가져옴"""
    user = g.get_user(username)
    repos = user.get_repos()  # 사용자의 레포지토리 가져오기

    repo_list = []
    for repo in repos:
        repo_list.append({
            "name": repo.name,
            "description": repo.description
        })

    return repo_list

# 사용 예시
username = input()

# 1. 프로필 README 가져오기
profile_readme_content = get_github_profile_readme(username)
print("README 내용:")
print(profile_readme_content)

# 2. 사용자의 레포지토리 목록 가져오기
repos = get_user_repos(username)
print("\n레포지토리 목록:")
for repo in repos:
    print(f"Repo Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print("\n")
