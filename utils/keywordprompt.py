from langchain.prompts import PromptTemplate

def get_star_keywords_prompt_template():
    # STAR 기법을 적용한 핵심 키워드 추출 프롬프트 (한글과 영어만 허용하도록 지시 추가)
    template = """
    Based on the following GitHub activity data, extract key keywords and phrases using the STAR method (Situation, Task, Action, Result) for each key project.
    The extracted data should include important keywords that describe the user's involvement in **Korean and English only**.

    - Projects: For each project, use the STAR method to extract keywords about the user's involvement in **Korean and English only**:
        - **Situation**: Extract keywords that describe the context or background of the project.
        - **Task**: Extract keywords that define the specific challenge or responsibility the user had.
        - **Action**: Extract keywords that describe the actions the user took to address the challenge or responsibility.
        - **Result**: Extract keywords that highlight the outcomes or results of the user's actions.

    The output should **only contain Korean and English words**, and must be in a structured format that can be stored in MongoDB.
    
    GitHub Activity Data:
    {github_data}
    """
    
    # 프롬프트에 사용할 변수 설정 (GitHub 데이터를 입력받음)
    return PromptTemplate(template=template, input_variables=["github_data"])

