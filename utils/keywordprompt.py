from langchain.prompts import PromptTemplate

def get_resume_keywords_prompt_template():
    """
    GitHub 활동 데이터로부터 이력서의 각 섹션에 필요한 정보를 추출하는 프롬프트.
    """
    template = """
    너는 사용자의 추출한 레포지토리의 정보들을 활용해서 다음과 같은 양식의 이력서를 만들어야 해. 이 이력서를 만들 수 있을 정보들을 토큰을 이용해서 추출하고 정보를 얻을 수 없는 경우에는 NULL을 입력해서 반환해.
    
    ## Skills


    ## Languages


    ## Interests


    $$
    \\small \\textbf  \\
    \\Huge \\textbf name \\
    \\small AI(LLM)-Developer
    $$

    <aside>
    📍 Location: example, South Korea
    </aside>
    <aside>
    ☎️ Contact: 010-xxxx-xxxx
    </aside>
    <aside>
    📧 Email: example@example.com
    </aside>

    ### 🧑‍💻 About Me
    안녕하세요! **’Comfort-Zone에서 벗어나 끊임없이 도전을 하는 개발자’** name입니다.

    - **Self-Motivation**: 어떤 일이든 관심이 생기면 망설임 없이 도전하여 실행에 옮깁니다.
    - **Optimization-Driven**: 코드 한 줄까지도 성능 최적화에 집중하여 시스템의 효율성을 극대화합니다.
    - **Collaborative Growth**: 개인적 성장을 넘어서, 함께 발전하는 문화를 추구합니다.

    ### 🏢 Work Experience
    **experience_years - experience_years_end**
    **Job Title** - ***example Company***

    **Project Name:** project_name
    - project_description
    - Technologies: technologies_used

    ### 🎓 Education
    **education_start - education_end**
    **degree_name** - **example University**

    ### 🏆 Awards
    **award_date**
    **award_name** - **example Organization**
    - Project: project_name_award
    - Achievements: achievements

    ### 🤼 Projects
    **project_start - project_end**
    **project_title** - **example Company**
    - Technologies: project_technologies
    - Achievements: project_achievements

    ## Generated GitHub Profile
    GitHub Activity Data:
    {github_data}
    """

    return PromptTemplate(template=template, input_variables=["github_data"])


