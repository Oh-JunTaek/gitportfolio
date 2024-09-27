from langchain.prompts import PromptTemplate

def get_prompt_template():
    # STAR 기법을 적용한 이력서 작성 프롬프트 (한글로 작성하도록 추가)
    template = """
    Based on the following GitHub activity data, generate a professional resume in Markdown format using the STAR method (Situation, Task, Action, Result) for each key project.
    The resume should be written in Korean and include the following sections: Personal Information, Summary, Projects, Skills, and Education.

    - Personal Information: Assume the user's name is {name}.
    - Summary: Summarize the user's professional experience and key contributions in Korean.
    - Projects: For each project, use the STAR method to describe the user's involvement in Korean:
        - **Situation**: Describe the context or background of the project.
        - **Task**: Define the specific challenge or responsibility the user had.
        - **Action**: Detail the actions the user took to address the challenge or responsibility.
        - **Result**: Highlight the outcomes or results of the user's actions, including any measurable improvements or accomplishments.
    - Skills: List the programming languages, tools, and technologies based on the user's GitHub activity.
    - Education: Provide an education section using placeholder data for now.

    The resume should be in Markdown format.
    
    GitHub Activity Data:
    {github_data}
    """
    
    # STAR 기법을 기반으로 각 프로젝트를 설명하는 프롬프트를 설정합니다.
    # Situation(상황): 프로젝트의 배경과 상황을 설명.
    # Task(과제): 사용자에게 부여된 특정 과제나 도전 과제를 기술.
    # Action(행동): 사용자가 문제 해결을 위해 취한 구체적인 행동.
    # Result(결과): 사용자가 달성한 성과 또는 결과를 설명.

    # 프롬프트에 사용할 변수 설정 (사용자 이름과 GitHub 데이터를 입력받음)
    return PromptTemplate(template=template, input_variables=["name", "github_data"])
