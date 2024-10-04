from langchain.prompts import PromptTemplate

def get_prompt_template_html():
    # STAR 기법을 적용한 이력서 작성 프롬프트 (HTML 형식으로 작성)
    template = """
    Based on the following GitHub activity data, generate a professional resume in HTML format using the STAR method (Situation, Task, Action, Result) for each key project.
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

    The resume should be in HTML format using appropriate HTML tags for headings, paragraphs, and lists (e.g., <h1>, <p>, <ul>, <li>, <strong>).
    
    GitHub Activity Data:
    {github_data}
    """
    
    # HTML 형식으로 각 프로젝트를 설명하는 프롬프트를 설정합니다.
    return PromptTemplate(template=template, input_variables=["name", "github_data"])