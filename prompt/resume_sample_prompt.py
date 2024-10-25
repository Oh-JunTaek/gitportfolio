from langchain.prompts import PromptTemplate

def get_resume_sample_prompt_template():
    # 샘플 이력서 양식을 기반으로 프롬프트 생성 (제목은 영어, 내용은 한글)
    template = """
    You will generate a professional resume in the following format based on the provided data. Replace personal or institution names with 'example' where applicable. Section titles will be in English, and content will be in Korean.

    ## Skills
    - Python, Java
    - PyTorch
    - FastAPI
    - React, MUI
    - PostgreSQL, MongoDB, Elastic Search
    - Langchain, RAG
    - Docker, AWS(EC2)
    - Git, Jira, Slack

    ## Languages
    - Korean
    - English

    ## Interests
    💻 Development
    🤖 New-Tech
    🏃‍♂️ Running
    🧑‍🍳 Cooking

    $$
    \\small \\textbf {} \\
    \\Huge \\textbf {{name}} \\
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
    안녕하세요! **’Comfort-Zone에서 벗어나 끊임없이 도전을 하는 개발자’** {name} 입니다.

    - **Self-Motivation**: 어떤 일이든 관심이 생기면 망설임 없이 도전하여 실행에 옮깁니다.
    - **Optimization-Driven**: 코드 한 줄까지도 성능 최적화에 집중하여 시스템의 효율성을 극대화합니다.
    - **Collaborative Growth**: 개인적 성장을 넘어서, 함께 발전하는 문화를 추구합니다.

    ### 🏢 Work Experience
    **{experience_years} - {experience_years_end}**
    **Job Title** - ***example Company***

    **Project Name:** {project_name}
    - {project_description}
    - Technologies: {technologies_used}

    ### 🎓 Education
    **{education_start} - {education_end}**
    **{degree_name}** - **example University**

    ### 🏆 Awards
    **{award_date}**
    **{award_name}** - **example Organization**
    - Project: {project_name_award}
    - Achievements: {achievements}

    ### 🤼 Projects
    **{project_start} - {project_end}**
    **{project_title}** - **example Company**
    - Technologies: {project_technologies}
    - Achievements: {project_achievements}

    ## Generated GitHub Profile
    {github_profile}

    """

    # 사용자 데이터 및 프로젝트 정보 입력
    return PromptTemplate(template=template, input_variables=[
        "name", "experience_years", "experience_years_end", 
        "project_name", "project_description", "technologies_used", 
        "education_start", "education_end", "degree_name", 
        "award_date", "award_name", "project_name_award", 
        "achievements", "project_start", "project_end", 
        "project_title", "project_technologies", "project_achievements", 
        "github_profile"
    ])
