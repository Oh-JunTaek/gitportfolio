from models.llama import get_llama_model
from utils.prompt import get_prompt_template
from utils.github_api import get_repo_info

def save_as_markdown(content, file_name="resume.md"):
    """답변을 .md 파일로 저장하는 함수"""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # GitHub 레포지토리 데이터를 처리하여 프롬프트에 넣을 데이터 생성
    repo_name = "Oh-JunTaek/MiniBaseball"  # 정확한 형식으로 레포지토리 입력
    repo = get_repo_info(repo_name)
    github_data = f"Repository Name: {repo.full_name}\nDescription: {repo.description}"

    # 프롬프트에 name과 github_data를 전달
    prompt = get_prompt_template()
    result = get_llama_model(prompt.format(name="JunTaek Oh", github_data=github_data))

    # 결과를 .md 파일로 저장
    save_as_markdown(result)
    print("이력서가 .md 파일로 저장되었습니다.")
