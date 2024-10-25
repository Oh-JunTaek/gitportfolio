from utils.find_readme import get_github_profile_readme, get_user_repos
from utils.company_info import get_company_from_json
from models import get_openai_model_and_check_moderation

def main():
    # 1. 회사 정보 가져오기 (사전 등록된 JSON 파일에서)
    company_name = "카카오"  # 회사 이름을 하드코딩 또는 외부에서 가져오는 방식으로
    company_info = get_company_from_json(company_name)

    if not company_info:
        print(f"'{company_name}'에 대한 사전 등록된 정보가 없습니다.")
        return

    # 2. GitHub 정보 가져오기 (사전 입력된 사용자 이름)
    github_username = "M-Yadolahi"  # GitHub 사용자 이름을 하드코딩 또는 외부에서 가져오는 방식으로
    github_readme = get_github_profile_readme(github_username)
    github_repos = get_user_repos(github_username)

    # 3. 프롬프트 구성
    sample_prompt = f"""
    답변은 한국어로 생성하세요. 당신은 해당 기업에 지원하는 지원자입니다. 직접적인 기업에 대한 언급은 하지 마세요. 비유적 표현이 포함되면 좋습니다. Generate an 'About Me' based on the following information:

    Company Information:
    - Name: {company_info['name']}
    - Slogan: {company_info['slogan']}
    - Description: {company_info['description']}
    - Values: {', '.join(company_info['values'])}

    GitHub Profile:
    {github_readme}

    GitHub Repositories:
    
    'about me'는 다음과 같은 양식으로 생성하세요.
    주어진 정보와 관련있는 1~2단어: 그 단어의 의미가 담긴 인재상 풀이
    예시 'about me'는 다음과 같이 1줄로 3개 생성하세요.
    답변을 생성할 때 README와 깃허브 프로젝트를 최대한 반영하고 없으면 기업정보를 기반으로 생성하세요.
    시적인(문학적인) 표현을 담아서 생성하세요.
    Proactive Development: 필요한 미래를 앞당기기 위해 새로운 도전에 적극적으로 임합니다.
    """
    for repo in github_repos:
        sample_prompt += f"- {repo['name']}: {repo['description']}\n"

    # 4. OpenAI 모델 호출하여 About Me 생성 및 검열
    about_me = get_openai_model_and_check_moderation(sample_prompt)

    # 5. 생성된 About Me 출력
    if about_me:
        print("\nGenerated About Me:\n")
        print(about_me)
    else:
        print("부적절한 콘텐츠로 인해 결과가 반환되지 않았습니다.")

# 메인 함수 실행
if __name__ == "__main__":
    main()
