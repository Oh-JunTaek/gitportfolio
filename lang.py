from github import Github
import json
import os

# GitHub 인증 설정
github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token)
repo_name = "Oh-JunTaek/gitportfolio"  # 예제 레포지토리 이름

repo = g.get_repo(repo_name)

# 언어 정보
languages = repo.get_languages()
primary_languages = ", ".join(languages.keys())
print(f"사용된 언어: {primary_languages}")

# 종속성 파일 목록과 프레임워크 목록을 JSON에서 로드
with open("data/dependency_files.json", "r") as f:
    dependency_files = json.load(f)

with open("data/frameworks.json", "r") as f:
    frameworks_data = json.load(f)

# JSON에서 모든 종속성 파일을 합쳐서 하나의 리스트로 만들기
all_dependency_files = [file for files in dependency_files.values() for file in files]

# 실제 사용된 프레임워크를 저장할 리스트
used_frameworks = set()

# 종속성 파일 분석 및 라이브러리 매칭
contents = repo.get_contents("")
for content_file in contents:
    if content_file.name in all_dependency_files:
        file_content = repo.get_contents(content_file.path).decoded_content.decode()
        
        # 언어별로 프레임워크와 매칭
        for lang in languages.keys():
            if lang in frameworks_data:
                for framework in frameworks_data[lang]:
                    # 라이브러리 이름이 종속성 파일에 존재하는지 확인
                    if framework.lower() in file_content.lower():
                        used_frameworks.add(framework)

# 토픽에서 프레임워크 추출
topics = repo.get_topics()
for topic in topics:
    for lang in languages.keys():
        if lang in frameworks_data:
            for framework in frameworks_data[lang]:
                if framework.lower() in topic.lower():
                    used_frameworks.add(framework)

# 최종 결과 출력
print("\n--- 최종 결과 ---")
print(f"사용 언어: {primary_languages}")
print(f"사용 프레임워크: {', '.join(sorted(used_frameworks))}")
